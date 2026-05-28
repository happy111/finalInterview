#!/usr/bin/env python3
"""
Simple test script to verify the FastAPI application structure
"""
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported successfully"""
    try:
        from app.config import settings
        print("✓ Config imported successfully")
        
        from app.database import get_db, engine
        print("✓ Database module imported successfully")
        
        from app.models.user import User
        from app.models.item import Item
        print("✓ Models imported successfully")
        
        from app.schemas.user import UserCreate, UserResponse
        from app.schemas.item import ItemCreate, ItemResponse
        print("✓ Schemas imported successfully")
        
        from app.crud.user import user
        from app.crud.item import item
        print("✓ CRUD modules imported successfully")
        
        from app.api.deps import get_current_user
        print("✓ API dependencies imported successfully")
        
        from app.main import app
        print("✓ Main application imported successfully")
        
        print("\n🎉 All imports successful! The application structure is correct.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_config():
    """Test configuration loading"""
    try:
        from app.config import settings
        print(f"✓ Database URL: {settings.database_url}")
        print(f"✓ Secret Key: {settings.secret_key[:10]}...")
        print(f"✓ Environment: {settings.environment}")
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

if __name__ == "__main__":
    print("Testing FastAPI CRUD Application...\n")
    
    success = True
    success &= test_imports()
    success &= test_config()
    
    if success:
        print("\n✅ All tests passed! The application is ready to run.")
        print("\nTo start the application, run:")
        print("  python run.py")
        print("  or")
        print("  uvicorn app.main:app --reload")
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        sys.exit(1) 