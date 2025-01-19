from sqlalchemy import create_engine  # Engine connects to the database
from sqlalchemy.orm import sessionmaker  # For managing database sessions
from sqlalchemy.ext.declarative import declarative_base  # Base class for all models

# Database connection URL (SQLite in this case)
SQLALCHEMY_DB_URL = "sqlite:///./sql_app.db"  # SQLite database file in the current directory

# Alternative MySQL connection URL (commented out for now)
# DB_URL = "mysql://root:root@localhost/first_db"

# Create the SQLAlchemy engine for connecting to the database
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})

# Session maker for creating and managing database sessions
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for defining ORM models (User inherits from this)
Base = declarative_base()
