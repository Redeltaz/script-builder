from fastapi import APIRouter, HTTPException
from typing import List

from ..crud import user_crud
from ..schemas import User, UserCreate, UserUpdate
from ..utils import get_actual_date

user_router = APIRouter()

@user_router.get("/", response_model=List[User])
def get_users():
    """
    get all users
    """
    users_db = user_crud.read_all()
    
    return users_db

@user_router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    """
    get user by id
    """
    user_db = user_crud.read(user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user_db

@user_router.post("/", response_model=User)
def create_user(request_body: UserCreate):
    """
    create user
    """
    user_params = dict(request_body)
    actual_date = get_actual_date()
    user_db = user_crud.read_by_email(user_params["email"])
    
    if user_db:
        raise HTTPException(status_code=409, detail="User with this email already exist")
    
    user_params["is_superuser"] = False
    user_params["is_admin"] = False
    user_params["creation_date"] = actual_date
    user_params["update_date"] = actual_date
    
    user_db = user_crud.create(user_params)
    
    return user_db

@user_router.put("/{user_id}", response_model=User)
def update_user(
    user_id: str,
    request_body: UserUpdate
):
    """
    update user
    """
    user_params = dict(request_body)
    user_db = user_crud.read_by_email(user_params["email"])
    
    if user_db:
        raise HTTPException(status_code=409, detail="User with this email already exist")
    
    user_params["update_date"] = get_actual_date()
    
    user_db = user_crud.read(user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_db = user_crud.update(user_id, user_params)
    
    return user_db

@user_router.delete("/{user_id}")
def delete_user(user_id: str):
    """
    delete user
    """
    user_db = user_crud.read(user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_db = user_crud.delete(user_id)
    
    return user_db