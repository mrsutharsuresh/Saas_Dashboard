from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any

# Authentication
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    role: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Projects & Clients
class ClientCreate(BaseModel):
    name: str
    phone: str

class ClientResponse(ClientCreate):
    id: int
    owner_id: int
    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    title: str
    survey_number: Optional[str] = None
    portal_data: Optional[str] = "{}" # JSON string

class ProjectCreate(ProjectBase):
    client_id: Optional[int] = None

class ProjectResponse(ProjectBase):
    id: int
    status: str
    owner_id: int
    client: Optional[ClientResponse] = None
    class Config:
        from_attributes = True

# Scraper (Existing)
class ScrapeRequest(BaseModel):
    client_id: str
    portal_type: str 
    survey_number: Optional[str] = None
    owner_name: Optional[str] = None

class ScrapeResponse(BaseModel):
    task_id: str
    status: str
    message: str
    data: Optional[Dict[str, Any]] = None
