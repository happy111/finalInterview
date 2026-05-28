from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from category.schemas import CategoryCreate, CategoryResponse
from category import services
from category.retry_service import retry_request

router = APIRouter(prefix="/category", tags=["Category"])

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return services.get_all_categories(db)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return services.get_category(db, category_id)


@router.post("/", response_model=CategoryResponse)
def create_category(data: CategoryCreate, db: Session = Depends(get_db)):

    # Retry applied here
    retry_request("https://httpbin.org/status/500")

    return services.create_category(db, data)


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, data: CategoryCreate, db: Session = Depends(get_db)):
    return services.update_category(db, category_id, data)


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return services.delete_category(db, category_id)
