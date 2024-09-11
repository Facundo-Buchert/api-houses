from pydantic import BaseModel
from typing import List

class HouseBase(BaseModel):
    title: str
    walink: str
    type: str
    operation: str
    expenses: str
    rooms: str
    bathrooms: str
    toilettes: str
    garages: str
    coveredGarage: str
    pool: str
    grill: str
    floors: str
    new: str
    antique: str
    surface: str
    coveredSurface: str
    city: str
    zone: str
    street: str
    height: str
    price: str
    currency: str
    paymentMethods: str
    description: str
    img: List[str]

class HouseCreate(HouseBase):
    pass

class House(HouseBase):
    id: int

    class Config:
        orm_mode = True
