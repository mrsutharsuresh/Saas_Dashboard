from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String, default="professional")  # professional / admin
    
    projects = relationship("Project", back_populates="owner")
    clients = relationship("Client", back_populates="owner")

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="clients")
    projects = relationship("Project", back_populates="client")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    survey_number = Column(String)
    # Generic JSON blob for portal specific data (Flexible)
    portal_data = Column(Text, default="{}") 
    status = Column(String, default="pending")
    owner_id = Column(Integer, ForeignKey("users.id"))
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=True)
    
    owner = relationship("User", back_populates="projects")
    client = relationship("Client", back_populates="projects")
    
class NotificationDraft(Base):
    __tablename__ = "notification_drafts"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    content = Column(String)
    status = Column(String, default="pending") # pending, approved, rejected, sent
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
