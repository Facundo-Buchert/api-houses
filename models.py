from sqlalchemy import Column, Integer, String, Text, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    walink = Column(Text)
    type = Column(Text)
    operation = Column(Text)
    expenses = Column(Text)
    rooms = Column(Text)
    bathrooms = Column(Text)
    toilettes = Column(Text)
    garages = Column(Text)
    coveredGarage = Column(Text)
    pool = Column(Text)
    grill = Column(Text)
    floors = Column(Text)
    new = Column(Text)
    antique = Column(Text)
    surface = Column(Text)
    coveredSurface = Column(Text)
    city = Column(Text)
    zone = Column(Text)
    street = Column(Text)
    height = Column(Text)
    price = Column(Text)
    currency = Column(Text)
    paymentMethods = Column(Text)
    description = Column(Text)
    img = Column(ARRAY(Text))
