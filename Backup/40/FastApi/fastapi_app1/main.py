from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from category.routes import router as category_router

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Category API with Retry")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(category_router)

@app.get("/")
def root():
    return {"message": "FastAPI Category Service Running!"}
