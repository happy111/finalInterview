from typing import List, Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    def get_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Item]:
        return (
            db.query(Item)
            .filter(Item.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_owner_and_id(
        self, db: Session, *, owner_id: int, item_id: int
    ) -> Optional[Item]:
        return (
            db.query(Item)
            .filter(Item.owner_id == owner_id, Item.id == item_id)
            .first()
        )

    def create(self, db: Session, *, obj_in: ItemCreate, owner_id: int) -> Item:
        db_obj = Item(
            title=obj_in.title,
            description=obj_in.description,
            price=obj_in.price,
            owner_id=owner_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_by_owner(
        self, db: Session, *, owner_id: int, item_id: int, obj_in: ItemUpdate
    ) -> Optional[Item]:
        db_obj = self.get_by_owner_and_id(db, owner_id=owner_id, item_id=item_id)
        if not db_obj:
            return None
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

    def remove_by_owner(
        self, db: Session, *, owner_id: int, item_id: int
    ) -> Optional[Item]:
        db_obj = self.get_by_owner_and_id(db, owner_id=owner_id, item_id=item_id)
        if not db_obj:
            return None
        db.delete(db_obj)
        db.commit()
        return db_obj


item = CRUDItem(Item) 