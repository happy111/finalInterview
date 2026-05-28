from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_current_active_user
from app.crud.item import item
from app.database import get_db
from app.models.user import User
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate

router = APIRouter()


@router.get("/", response_model=List[ItemResponse])
def read_items(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Retrieve items for current user.
    """
    items = item.get_by_owner(db, owner_id=current_user.id, skip=skip, limit=limit)
    return items


@router.post("/", response_model=ItemResponse)
def create_item(
    *,
    db: Session = Depends(get_db),
    item_in: ItemCreate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    item_obj = item.create(db, obj_in=item_in, owner_id=current_user.id)
    return item_obj


@router.get("/{item_id}", response_model=ItemResponse)
def read_item(
    *,
    db: Session = Depends(get_db),
    item_id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    item_obj = item.get_by_owner_and_id(db, owner_id=current_user.id, item_id=item_id)
    if not item_obj:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )
    return item_obj


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(
    *,
    db: Session = Depends(get_db),
    item_id: int,
    item_in: ItemUpdate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Update an item.
    """
    item_obj = item.update_by_owner(
        db, owner_id=current_user.id, item_id=item_id, obj_in=item_in
    )
    if not item_obj:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )
    return item_obj


@router.delete("/{item_id}")
def delete_item(
    *,
    db: Session = Depends(get_db),
    item_id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    item_obj = item.remove_by_owner(db, owner_id=current_user.id, item_id=item_id)
    if not item_obj:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )
    return {"message": "Item deleted successfully"} 