# FastAPI CRUD Application

A modern FastAPI application with CRUD operations, MySQL database connection, and modular structure.

## Features

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **MySQL** - Database backend
- **JWT Authentication** - Secure token-based authentication
- **Modular Structure** - Clean, organized codebase
- **CRUD Operations** - Complete Create, Read, Update, Delete functionality
- **Pydantic Models** - Data validation and serialization
- **Alembic** - Database migrations
- **CORS Support** - Cross-origin resource sharing
- **Auto-generated API Documentation** - Swagger UI and ReDoc

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration settings
│   ├── database.py          # Database connection
│   ├── api/
│   │   ├── deps.py         # Dependencies
│   │   └── v1/
│   │       ├── api.py      # Main API router
│   │       └── endpoints/
│   │           ├── auth.py # Authentication endpoints
│   │           ├── users.py # User management
│   │           └── items.py # Item CRUD operations
│   ├── crud/
│   │   ├── base.py         # Base CRUD class
│   │   ├── user.py         # User CRUD operations
│   │   └── item.py         # Item CRUD operations
│   ├── models/
│   │   ├── user.py         # User model
│   │   └── item.py         # Item model
│   └── schemas/
│       ├── user.py         # User Pydantic schemas
│       └── item.py         # Item Pydantic schemas
├── alembic/                 # Database migrations
├── requirements.txt         # Python dependencies
├── config.env              # Environment variables
├── alembic.ini            # Alembic configuration
└── README.md              # This file
```

## Prerequisites

- Python 3.8+
- MySQL Server
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-crud-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL Database**
   ```sql
   CREATE DATABASE fastapi_crud;
   CREATE USER 'fastapi_user'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON fastapi_crud.* TO 'fastapi_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

5. **Configure Environment Variables**
   Edit `config.env` file with your database credentials:
   ```env
   DATABASE_URL=mysql+pymysql://fastapi_user:your_password@localhost:3306/fastapi_crud
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=fastapi_user
   DB_PASSWORD=your_password
   DB_NAME=fastapi_crud
   SECRET_KEY=your-secret-key-here-change-in-production
   ```

6. **Run Database Migrations**
   ```bash
   alembic upgrade head
   ```

## Running the Application

1. **Start the server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Access the application**
   - API Documentation: http://localhost:8000/docs
   - ReDoc Documentation: http://localhost:8000/redoc
   - Health Check: http://localhost:8000/health

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Login and get access token
- `GET /api/v1/auth/me` - Get current user info

### Users (Admin only)
- `GET /api/v1/users/` - List all users
- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/{user_id}` - Get user by ID
- `PUT /api/v1/users/{user_id}` - Update user
- `DELETE /api/v1/users/{user_id}` - Delete user

### Items (Authenticated users)
- `GET /api/v1/items/` - List user's items
- `POST /api/v1/items/` - Create a new item
- `GET /api/v1/items/{item_id}` - Get item by ID
- `PUT /api/v1/items/{item_id}` - Update item
- `DELETE /api/v1/items/{item_id}` - Delete item

## Usage Examples

### 1. Register a new user
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
     -H "Content-Type: application/json" \
     -d '{
       "email": "user@example.com",
       "username": "testuser",
       "full_name": "Test User",
       "password": "password123"
     }'
```

### 2. Login and get token
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=user@example.com&password=password123"
```

### 3. Create an item (with authentication)
```bash
curl -X POST "http://localhost:8000/api/v1/items/" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "My Item",
       "description": "This is my item",
       "price": 100
     }'
```

### 4. Get user's items
```bash
curl -X GET "http://localhost:8000/api/v1/items/" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Development

### Database Migrations
```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### Code Structure

The application follows a modular structure:

- **Models**: SQLAlchemy ORM models defining database tables
- **Schemas**: Pydantic models for request/response validation
- **CRUD**: Database operations layer
- **API**: FastAPI endpoints and routers
- **Dependencies**: Authentication and database session management

## Security Features

- **Password Hashing**: Uses bcrypt for secure password storage
- **JWT Tokens**: Secure token-based authentication
- **CORS**: Configurable cross-origin resource sharing
- **Input Validation**: Pydantic models ensure data validation
- **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection

## Production Deployment

1. **Update environment variables** for production settings
2. **Use a production ASGI server** like Gunicorn with Uvicorn workers
3. **Set up a reverse proxy** (Nginx/Apache)
4. **Configure SSL/TLS** certificates
5. **Set up proper logging** and monitoring
6. **Use environment-specific database** configurations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License. 