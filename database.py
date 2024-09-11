from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# URL de la base de datos PostgreSQL obtenida de una variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL")  # La URL debe ser definida como variable de entorno en el servidor.

# Crear el motor para SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crear una sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para declarar los modelos
Base = declarative_base()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
