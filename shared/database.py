"""
Database Manager

Shared database utilities and connection management.
"""

import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DatabaseManager:
    """Database connection and session management."""
    
    def __init__(self, database_url: str = None):
        """Initialize database manager with connection URL."""
        self.database_url = database_url or os.getenv('DATABASE_URL', 'sqlite:///./apps2.db')
        self.engine = create_engine(self.database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    
    def get_session(self):
        """Get a database session."""
        return self.SessionLocal()
    
    def create_tables(self):
        """Create all tables."""
        Base.metadata.create_all(bind=self.engine)
    
    def test_connection(self) -> bool:
        """Test database connection."""
        try:
            with self.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            return True
        except Exception as e:
            print(f"Database connection failed: {e}")
            return False
    
    def close(self):
        """Close database connection."""
        self.engine.dispose()
