from sqlalchemy.orm import Session
from . import models, schemas

def get_houses(db: Session):
    return db.query(models.House).all()

def create_house(db: Session, house: schemas.HouseCreate):
    db_house = models.House(**house.dict())
    db.add(db_house)
    db.commit()
    db.refresh(db_house)
    return db_house

def delete_house(db: Session, house_id: int):
    db_house = db.query(models.House).filter(models.House.id == house_id).first()
    if db_house:
        db.delete(db_house)
        db.commit()
