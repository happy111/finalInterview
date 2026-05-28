from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import user_routes

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD App")

app.include_router(user_routes.router)

@app.get("/")
def root():
    return {"message": "FastAPI with MySQL working!"}
