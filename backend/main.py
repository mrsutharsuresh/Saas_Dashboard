from fastapi import FastAPI, BackgroundTasks, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import List

from database import engine, Base, get_db
from models import User, Project, Client
import schemas
import auth
from engine import run_scraper_task
import uuid

# Create Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SaaS Dashboard API", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "SaaS Dashboard API is Running"}

# --- Auth Routes ---
@app.post("/auth/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = auth.get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/auth/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=schemas.UserResponse)
async def read_users_me(current_user: User = Depends(auth.get_current_user)):
    return current_user

# --- Project CRUD ---
@app.post("/projects/", response_model=schemas.ProjectResponse)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    new_project = Project(
        title=project.title,
        survey_number=project.survey_number,
        portal_data=project.portal_data,
        owner_id=current_user.id,
        client_id=project.client_id
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@app.get("/projects/", response_model=List[schemas.ProjectResponse])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    projects = db.query(Project).filter(Project.owner_id == current_user.id).offset(skip).limit(limit).all()
    return projects

# --- Scraper ---
@app.post("/scrape", response_model=schemas.ScrapeResponse)
async def trigger_scrape(request: schemas.ScrapeRequest, background_tasks: BackgroundTasks, current_user: User = Depends(auth.get_current_user)):
    task_id = str(uuid.uuid4())
    # Run scraping in the background
    background_tasks.add_task(run_scraper_task, request)
    return schemas.ScrapeResponse(
        task_id=task_id,
        status="queued",
        message="Scraping task started in background."
    )

