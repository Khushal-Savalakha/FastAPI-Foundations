from fastapi import FastAPI, Query, Depends  # FastAPI framework for quickly building web APIs and handling dependencies
from typing import Optional, List  # For type annotations to define optional fields and lists
from sqlalchemy import Column, String, Boolean, Integer  # For defining the schema of database tables
from pydantic import BaseModel  # For data validation and serialization/deserialization
from database import Base, engine, sessionLocal  # Custom database setup for SQLAlchemy Base and engine
from sqlalchemy.orm import session  # For creating and managing database sessions

# Explain the need for imports:
# - `FastAPI`: The core framework for building the API.
# - `Depends`: Dependency injection in FastAPI to handle shared resources like the database session.
# - `Query`: To define query parameters in API routes (not used here but kept for future use).
# - `BaseModel`: Used to define Pydantic models for input/output validation and serialization.
# - `session`: For interacting with the database using SQLAlchemy ORM.
# - `Base`: The declarative base class for defining SQLAlchemy models.
# - `engine`: Used to connect to the database and manage connections.
# - `sessionLocal`: Creates SQLAlchemy session instances to interact with the database.

# Define the User model (SQLAlchemy ORM model to map Python classes to database tables)
class User(Base):
    """
    SQLAlchemy ORM model representing the 'users' table in the database.

    Attributes:
        id (int): Primary key, unique for each user.
        email (str): Unique email address for the user.
        is_active (bool): Boolean field indicating if the user is active.
    """
    __tablename__ = "users"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Auto-incremented primary key
    email = Column(String, unique=True, index=True)  # Unique email column, indexed for faster lookups
    is_active = Column(Boolean, default=True)  # Indicates if the user is active (default: True)

# Define the UserSchema (Pydantic model for input/output validation)
class UserSchema(BaseModel):
    """
    Pydantic model for validating and serializing user data.
    
    Attributes:
        id (int): Unique identifier for the user.
        email (str): Email address of the user.
        is_active (bool): Indicates if the user is active.
    """
    id: int
    email: str
    is_active: bool

    class Config:
        """
        Configuration for Pydantic model.
        Enables `orm_mode` to work with SQLAlchemy ORM objects, allowing seamless serialization.
        """
        orm_mode = True

# Dependency to get a database session
def get_db():
    """
    Creates and provides a SQLAlchemy database session.
    Ensures the session is properly closed after the request is completed.
    """
    db = sessionLocal()  # Create a new database session
    try:
        yield db  # Provide the session to the route
    finally:
        db.close()  # Close the session to prevent resource leaks

# Automatically create all tables in the database if they don't already exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI()

# Route to create a new user
@app.post("/users", response_model=UserSchema)
def create_user(user: UserSchema, db: session = Depends(get_db)):
    """
    Create a new user in the database.

    Args:
        user (UserSchema): Pydantic model representing the user data.
        db (session): SQLAlchemy database session (injected via `Depends`).

    Returns:
        User: The newly created user as a SQLAlchemy object.
    """
    # Create a new User object from the input data
    u = User(email=user.email, is_active=user.is_active, id=user.id)
    db.add(u)  # Add the new user to the session
    db.commit()  # Commit the transaction to save changes to the database
    return u  # Return the created user (FastAPI uses `response_model` to format the response)

# Route to fetch all users
@app.get("/users", response_model=List[UserSchema])
def get_users(db: session = Depends(get_db)):
    """
    Fetch all users from the database.

    Args:
        db (session): SQLAlchemy database session (injected via `Depends`).

    Returns:
        List[User]: A list of all users in the database, formatted using the `UserSchema`.
    """
    return db.query(User).all()  # Query the database for all users and return the results
