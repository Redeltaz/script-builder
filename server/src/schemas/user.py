from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
    is_superuser: str
    is_admin: str
    
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    
class UserUpdate(BaseModel):
    username: str
    email: str
    password: str
    is_superuser: str
    is_admin: str