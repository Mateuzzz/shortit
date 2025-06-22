from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Adres bazy danych (SQLite przechowuje dane w pliku `tasks.db`)
SQLALCHEMY_DATABASE_URL = "sqlite:///./links.db"

# Silnik bazy danych
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}  # wymagane tylko dla SQLite
)

# Sesja bazy danych (każde zapytanie będzie ją używać)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Bazowa klasa dla modeli
Base = declarative_base()