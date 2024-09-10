from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base

class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    walink = Column(String)
    type = Column(String)
    operation = Column(String)
    expenses = Column(String)
    rooms = Column(Integer)
    bathrooms = Column(Integer)
    toilettes = Column(Integer)
    garages = Column(Integer)
    coveredGarage = Column(String)
    pool = Column(String)
    grill = Column(String)
    floors = Column(Integer)
    new = Column(String)
    antique = Column(String)
    surface = Column(Float)
    coveredSurface = Column(Float)
    city = Column(String)
    zone = Column(String)
    street = Column(String)
    height = Column(String)
    price = Column(Float)
    currency = Column(String)
    paymentMethods = Column(String)
    description = Column(String)
    img = Column(String)  # Las imágenes se almacenan como una cadena separada por comas
