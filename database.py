from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de la base de datos PostgreSQL obtenida de ElephantSQL, Supabase o cualquier otro servicio
DATABASE_URL = "postgresql://postgres:UDmnXVvrQvxabWCTQzSzoHKTIwvaGDVM@meticulous-empathy.railway.internal:5432/railway"

# Crear el motor para SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crear una sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para declarar los modelos
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
