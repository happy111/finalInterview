from sqlalchemy.orm import Session
from . import models, schemas

def get_categories(db: Session):
    return db.query(models.Category).all()


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def create_category(db: Session, data: schemas.CategoryCreate):
    new_cat = models.Category(name=data.name, description=data.description)
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return new_cat


def update_category(db: Session, category_id: int, data: schemas.CategoryCreate):
    category = get_category(db, category_id)
    if category:
        category.name = data.name
        category.description = data.description
        db.commit()
        db.refresh(category)
    return category


def delete_category(db: Session, category_id: int):
    category = get_category(db, category_id)
    if category:
        db.delete(category)
        db.commit()
    return category
