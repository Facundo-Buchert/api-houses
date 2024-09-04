from fastapi import FastAPI, HTTPException  # Importar HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las solicitudes de todos los orígenes. Ajusta esto para mayor seguridad.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todas las cabeceras (headers)
)

class House(BaseModel):
    id: int
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

houses = [
    House(id=1, title='DUPLEX RINCONES DE MANANTIALES', walink='', type='Duplex', operation='Venta', expenses='0', rooms='3', bathrooms='3', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Córdoba', zone='SurOeste', street='Av. Donosa', height='258', price='115000', currency='$US', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños...', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=2, title='DUPLEX RINCONES DE MANANTIALES', walink='', type='Duplex', operation='Venta', expenses='0', rooms='3', bathrooms='3', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Córdoba', zone='SurOeste', street='Av. Donosa', height='258', price='115000', currency='$US', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños...', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=3, title='DUPLEX RINCONES DE MANANTIALES', walink='', type='Duplex', operation='Venta', expenses='0', rooms='3', bathrooms='3', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Córdoba', zone='SurOeste', street='Av. Donosa', height='258', price='115000', currency='$US', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños...', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=4, title='DUPLEX RINCONES DE MANANTIALES', walink='', type='Duplex', operation='Venta', expenses='0', rooms='3', bathrooms='3', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Córdoba', zone='SurOeste', street='Av. Donosa', height='258', price='115000', currency='$US', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños...', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=5, title='DUPLEX RINCONES DE MANANTIALES', walink='', type='Duplex', operation='Venta', expenses='0', rooms='3', bathrooms='3', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Córdoba', zone='SurOeste', street='Av. Donosa', height='258', price='115000', currency='$US', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños...', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=6, title='DUPLEX RINCONES DE MANANTIALES', walink='', type='Duplex', operation='Venta', expenses='0', rooms='3', bathrooms='3', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Córdoba', zone='SurOeste', street='Av. Donosa', height='258', price='115000', currency='$US', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños...', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=7, title='DUPLEX RINCONES DE MANANTIALES', walink='', type='Duplex', operation='Venta', expenses='0', rooms='3', bathrooms='3', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Córdoba', zone='SurOeste', street='Av. Donosa', height='258', price='115000', currency='$US', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños...', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=8, title='DUPLEX RINCONES DE MANANTIALES', walink='', type='Duplex', operation='Venta', expenses='0', rooms='3', bathrooms='3', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Córdoba', zone='SurOeste', street='Av. Donosa', height='258', price='115000', currency='$US', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños...', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    
]

@app.get("/houses", response_model=List[House])
def get_houses():
    return houses

@app.get("/houses/{house_id}", response_model=House)
def get_house(house_id: int):
    house = next((h for h in houses if h.id == house_id), None)
    if house is None:
        raise HTTPException(status_code=404, detail="House not found")
    return house
