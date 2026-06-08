from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# MySQL Database Configuration
DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_NAME = "dbcrud"
DB_PORT = 3306

# Create Database URL
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Create Base Class for ORM Models
Base = declarative_base()

# Create Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
def init_db():
    Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
