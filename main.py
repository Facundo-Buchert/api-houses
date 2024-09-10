from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models import House as HouseModel
from database import Base, engine, get_db
from pydantic import BaseModel

app = FastAPI()

# Habilitar CORS para permitir solicitudes desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear las tablas en la base de datos (solo la primera vez)
Base.metadata.create_all(bind=engine)

# Modelo de datos para la API
class House(BaseModel):
    title: str
    walink: str
    type: str
    operation: str
    expenses: str
    rooms: int
    bathrooms: int
    toilettes: int
    garages: int
    coveredGarage: str
    pool: str
    grill: str
    floors: int
    new: str
    antique: str
    surface: float
    coveredSurface: float
    city: str
    zone: str
    street: str
    height: str
    price: float
    currency: str
    paymentMethods: str
    description: str
    img: List[str]

# GET - Obtener todas las casas
@app.get("/houses", response_model=List[House])
def get_houses(db: Session = Depends(get_db)):
    houses = db.query(HouseModel).all()
    return [House(**house.__dict__) for house in houses]

# POST - Crear una nueva casa
@app.post("/houses", response_model=House, status_code=status.HTTP_201_CREATED)
def create_house(house: House, db: Session = Depends(get_db)):
    db_house = HouseModel(
        title=house.title,
        walink=house.walink,
        type=house.type,
        operation=house.operation,
        expenses=house.expenses,
        rooms=house.rooms,
        bathrooms=house.bathrooms,
        toilettes=house.toilettes,
        garages=house.garages,
        coveredGarage=house.coveredGarage,
        pool=house.pool,
        grill=house.grill,
        floors=house.floors,
        new=house.new,
        antique=house.antique,
        surface=house.surface,
        coveredSurface=house.coveredSurface,
        city=house.city,
        zone=house.zone,
        street=house.street,
        height=house.height,
        price=house.price,
        currency=house.currency,
        paymentMethods=house.paymentMethods,
        description=house.description,
        img=",".join(house.img)  # Guardamos las imágenes como una cadena separada por comas
    )
    db.add(db_house)
    db.commit()
    db.refresh(db_house)
    return house

# PUT - Actualizar una casa existente
@app.put("/houses/{house_id}", response_model=House)
def update_house(house_id: int, updated_house: House, db: Session = Depends(get_db)):
    house = db.query(HouseModel).filter(HouseModel.id == house_id).first()
    if house is None:
        raise HTTPException(status_code=404, detail="House not found")
    
    for key, value in updated_house.dict().items():
        setattr(house, key, value)
    db.commit()
    return updated_house

# DELETE - Eliminar una casa
@app.delete("/houses/{house_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_house(house_id: int, db: Session = Depends(get_db)):
    house = db.query(HouseModel).filter(HouseModel.id == house_id).first()
    if house is None:
        raise HTTPException(status_code=404, detail="House not found")
    db.delete(house)
    db.commit()
    return {"message": "House deleted successfully"}
