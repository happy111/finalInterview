from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_current_active_superuser, get_current_active_user
from app.crud.user import user
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter()


@router.get("/", response_model=List[UserResponse])
def read_users(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=UserResponse)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate,
    current_user: User = Depends(get_current_active_superuser),
) -> Any:
    """
    Create new user.
    """
    user_obj = user.get_by_email(db, email=user_in.email)
    if user_obj:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user_obj = user.get_by_username(db, username=user_in.username)
    if user_obj:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user_obj = user.create(db, obj_in=user_in)
    return user_obj


@router.get("/{user_id}", response_model=UserResponse)
def read_user_by_id(
    user_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user_obj = user.get(db, id=user_id)
    if user_obj == current_user:
        return user_obj
    if not user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user_obj


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    user_in: UserUpdate,
    current_user: User = Depends(get_current_active_superuser),
) -> Any:
    """
    Update a user.
    """
    user_obj = user.get(db, id=user_id)
    if not user_obj:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system",
        )
    user_obj = user.update(db, db_obj=user_obj, obj_in=user_in)
    return user_obj


@router.delete("/{user_id}")
def delete_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    current_user: User = Depends(get_current_active_superuser),
) -> Any:
    """
    Delete a user.
    """
    user_obj = user.get(db, id=user_id)
    if not user_obj:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system",
        )
    user.remove(db, id=user_id)
    return {"message": "User deleted successfully"} 