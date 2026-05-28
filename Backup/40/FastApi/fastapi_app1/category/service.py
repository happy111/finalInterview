from sqlalchemy.orm import Session
from category.models import Category
from category.schemas import CategoryCreate
from category.exceptions import NotFoundException, BadRequestException

def get_all_categories(db: Session):
    return db.query(Category).all()

def get_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise NotFoundException("Category not found")
    return category

def create_category(db: Session, data: CategoryCreate):
    if db.query(Category).filter(Category.name == data.name).first():
        raise BadRequestException("Category already exists")

    new_cat = Category(name=data.name, description=data.description)
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return new_cat

def update_category(db: Session, category_id: int, data: CategoryCreate):
    category = get_category(db, category_id)
    category.name = data.name
    category.description = data.description
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = get_category(db, category_id)
    db.delete(category)
    db.commit()
    return {"message": "Category deleted"}
