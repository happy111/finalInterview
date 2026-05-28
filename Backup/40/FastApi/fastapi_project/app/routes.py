from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .retry_service import RetryService
from . import crud, schemas

router = APIRouter(prefix="/api/category", tags=["Category"])

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.post("/", response_model=schemas.CategoryResponse)
def create_category(body: schemas.CategoryCreate, db: Session = Depends(get_db)):
    
    # Retry external API before creating
    retry = RetryService()
    try:
        retry.call_api("https://httpbin.org/status/500")
    except Exception as e:
        raise HTTPException(status_code=503, detail="External API failed after retries")

    return crud.create_category(db, body)


@router.get("/{category_id}", response_model=schemas.CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)
    if not category:
        raise HTTPException(404, "Category Not Found")
    return category


@router.put("/{category_id}", response_model=schemas.CategoryResponse)
def update_category(category_id: int, body: schemas.CategoryCreate, db: Session = Depends(get_db)):
    category = crud.update_category(db, category_id, body)
    if not category:
        raise HTTPException(404, "Category Not Found")
    return category


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.delete_category(db, category_id)
    if not category:
        raise HTTPException(404, "Category Not Found")
    return {"message": "Deleted successfully"}
