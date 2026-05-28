#!/usr/bin/env python3
"""
Database setup script for FastAPI CRUD Application
"""
import sys
import os
from sqlalchemy import create_engine, text
from app.config import settings

def create_database():
    """Create the database if it doesn't exist"""
    try:
        # Create engine without database name
        base_url = f"mysql+pymysql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}"
        engine = create_engine(base_url)
        
        with engine.connect() as conn:
            # Create database if it doesn't exist
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {settings.db_name}"))
            conn.commit()
            print(f"✓ Database '{settings.db_name}' created successfully")
            
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        print("\nPlease make sure:")
        print("1. MySQL server is running")
        print("2. User credentials are correct in config.env")
        print("3. User has CREATE DATABASE privileges")
        return False
    
    return True

def create_tables():
    """Create all tables"""
    try:
        from app.database import engine
        from app.models import user, item
        
        # Create all tables
        user.Base.metadata.create_all(bind=engine)
        item.Base.metadata.create_all(bind=engine)
        
        print("✓ All tables created successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        return False

def test_connection():
    """Test database connection"""
    try:
        from app.database import engine
        
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✓ Database connection successful")
            return True
            
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def main():
    print("Setting up database for FastAPI CRUD Application...\n")
    
    # Test connection first
    if not test_connection():
        print("\nPlease check your database configuration in config.env")
        return
    
    # Create database
    if not create_database():
        return
    
    # Create tables
    if not create_tables():
        return
    
    print("\n✅ Database setup completed successfully!")
    print("\nYou can now run the application with:")
    print("  python run.py")

if __name__ == "__main__":
    main() 