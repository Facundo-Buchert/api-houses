from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definición del modelo House
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

# Base de datos simulada en memoria
houses = [
    House(id=1, title='DUPLEX EN NUEVA CÓRDOBA', walink='', type='Duplex', operation='Venta', expenses='0', rooms='1', bathrooms='1', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Nueva Córdoba', zone='SurOeste', street='Av. Donosa', height='258', price='115000', currency='$US', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños... Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vulputate, augue quis consectetur tempus, tortor augue vestibulum velit, quis sagittis nibh ex a orci. In feugiat leo eu dolor faucibus, vel fringilla odio laoreet. Quisque non mattis mauris. Duis congue malesuada urna non tempor. Mauris metus erat, rhoncus vitae elementum nec, tincidunt ac libero. Mauris vel lorem aliquet, porttitor quam non, accumsan ante. Quisque elementum finibus metus vitae accumsan. Praesent pulvinar molestie risus sit amet scelerisque. Vestibulum est enim, lobortis in hendrerit at, auctor et mi. Curabitur aliquet massa nec orci tempus, ut consectetur leo suscipit. Maecenas semper feugiat augue vel dapibus. Etiam ut mi erat. Integer malesuada enim non purus tempus, at vehicula arcu euismod. Sed dui turpis, fringilla vitae felis id, auctor semper diam. Sed faucibus vulputate diam et imperdiet. Vestibulum ac lectus quis ipsum congue molestie et mattis magna. Quisque porta hendrerit mollis. Donec a euismod lectus, ut porttitor nisi. Aenean tempus, justo eget varius gravida, mi sem sollicitudin leo, ut aliquam enim sem sit amet augue. Maecenas blandit erat sit amet mi vehicula luctus sit amet quis urna. Aenean sit amet molestie nisl. Ut consequat ex ante.', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=2, title='TERRENO EN NUEVA CÓRDOBA', walink='', type='Terreno', operation='Venta', expenses='0', rooms='2', bathrooms='2', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Nueva Córdoba', zone='SurOeste', street='Av. Lautaro', height='258', price='155000', currency='$ARS', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños... Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vulputate, augue quis consectetur tempus, tortor augue vestibulum velit, quis sagittis nibh ex a orci. In feugiat leo eu dolor faucibus, vel fringilla odio laoreet. Quisque non mattis mauris. Duis congue malesuada urna non tempor. Mauris metus erat, rhoncus vitae elementum nec, tincidunt ac libero. Mauris vel lorem aliquet, porttitor quam non, accumsan ante. Quisque elementum finibus metus vitae accumsan. Praesent pulvinar molestie risus sit amet scelerisque. Vestibulum est enim, lobortis in hendrerit at, auctor et mi. Curabitur aliquet massa nec orci tempus, ut consectetur leo suscipit. Maecenas semper feugiat augue vel dapibus. Etiam ut mi erat. Integer malesuada enim non purus tempus, at vehicula arcu euismod. Sed dui turpis, fringilla vitae felis id, auctor semper diam. Sed faucibus vulputate diam et imperdiet. Vestibulum ac lectus quis ipsum congue molestie et mattis magna. Quisque porta hendrerit mollis. Donec a euismod lectus, ut porttitor nisi. Aenean tempus, justo eget varius gravida, mi sem sollicitudin leo, ut aliquam enim sem sit amet augue. Maecenas blandit erat sit amet mi vehicula luctus sit amet quis urna. Aenean sit amet molestie nisl. Ut consequat ex ante.', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=3, title='CASA EN BARRIO JARDIN', walink='', type='Casa', operation='Venta', expenses='0', rooms='3', bathrooms='2', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Barrio Jardin', zone='SurOeste', street='Av. Alberdi', height='258', price='85000', currency='$ARS', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños... Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vulputate, augue quis consectetur tempus, tortor augue vestibulum velit, quis sagittis nibh ex a orci. In feugiat leo eu dolor faucibus, vel fringilla odio laoreet. Quisque non mattis mauris. Duis congue malesuada urna non tempor. Mauris metus erat, rhoncus vitae elementum nec, tincidunt ac libero. Mauris vel lorem aliquet, porttitor quam non, accumsan ante. Quisque elementum finibus metus vitae accumsan. Praesent pulvinar molestie risus sit amet scelerisque. Vestibulum est enim, lobortis in hendrerit at, auctor et mi. Curabitur aliquet massa nec orci tempus, ut consectetur leo suscipit. Maecenas semper feugiat augue vel dapibus. Etiam ut mi erat. Integer malesuada enim non purus tempus, at vehicula arcu euismod. Sed dui turpis, fringilla vitae felis id, auctor semper diam. Sed faucibus vulputate diam et imperdiet. Vestibulum ac lectus quis ipsum congue molestie et mattis magna. Quisque porta hendrerit mollis. Donec a euismod lectus, ut porttitor nisi. Aenean tempus, justo eget varius gravida, mi sem sollicitudin leo, ut aliquam enim sem sit amet augue. Maecenas blandit erat sit amet mi vehicula luctus sit amet quis urna. Aenean sit amet molestie nisl. Ut consequat ex ante.', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=4, title='DUPLEX EN BARRIO JARDIN', walink='', type='Duplex', operation='Venta', expenses='0', rooms='4', bathrooms='3', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Barrio Jardin', zone='SurOeste', street='Av. Rivadavia', height='258', price='195000', currency='$US', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños... Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vulputate, augue quis consectetur tempus, tortor augue vestibulum velit, quis sagittis nibh ex a orci. In feugiat leo eu dolor faucibus, vel fringilla odio laoreet. Quisque non mattis mauris. Duis congue malesuada urna non tempor. Mauris metus erat, rhoncus vitae elementum nec, tincidunt ac libero. Mauris vel lorem aliquet, porttitor quam non, accumsan ante. Quisque elementum finibus metus vitae accumsan. Praesent pulvinar molestie risus sit amet scelerisque. Vestibulum est enim, lobortis in hendrerit at, auctor et mi. Curabitur aliquet massa nec orci tempus, ut consectetur leo suscipit. Maecenas semper feugiat augue vel dapibus. Etiam ut mi erat. Integer malesuada enim non purus tempus, at vehicula arcu euismod. Sed dui turpis, fringilla vitae felis id, auctor semper diam. Sed faucibus vulputate diam et imperdiet. Vestibulum ac lectus quis ipsum congue molestie et mattis magna. Quisque porta hendrerit mollis. Donec a euismod lectus, ut porttitor nisi. Aenean tempus, justo eget varius gravida, mi sem sollicitudin leo, ut aliquam enim sem sit amet augue. Maecenas blandit erat sit amet mi vehicula luctus sit amet quis urna. Aenean sit amet molestie nisl. Ut consequat ex ante.', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=5, title='DEPARTAMENTO ZONA MANANTIALES', walink='', type='Departamento', operation='Alquiler', expenses='0', rooms='1', bathrooms='1', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Manantiales', zone='SurOeste', street='Av. Belgrano', height='258', price='15000', currency='$US', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños... Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vulputate, augue quis consectetur tempus, tortor augue vestibulum velit, quis sagittis nibh ex a orci. In feugiat leo eu dolor faucibus, vel fringilla odio laoreet. Quisque non mattis mauris. Duis congue malesuada urna non tempor. Mauris metus erat, rhoncus vitae elementum nec, tincidunt ac libero. Mauris vel lorem aliquet, porttitor quam non, accumsan ante. Quisque elementum finibus metus vitae accumsan. Praesent pulvinar molestie risus sit amet scelerisque. Vestibulum est enim, lobortis in hendrerit at, auctor et mi. Curabitur aliquet massa nec orci tempus, ut consectetur leo suscipit. Maecenas semper feugiat augue vel dapibus. Etiam ut mi erat. Integer malesuada enim non purus tempus, at vehicula arcu euismod. Sed dui turpis, fringilla vitae felis id, auctor semper diam. Sed faucibus vulputate diam et imperdiet. Vestibulum ac lectus quis ipsum congue molestie et mattis magna. Quisque porta hendrerit mollis. Donec a euismod lectus, ut porttitor nisi. Aenean tempus, justo eget varius gravida, mi sem sollicitudin leo, ut aliquam enim sem sit amet augue. Maecenas blandit erat sit amet mi vehicula luctus sit amet quis urna. Aenean sit amet molestie nisl. Ut consequat ex ante.', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=6, title='DEPARTAMENTO ZONA MANANTIALES', walink='', type='Departamento', operation='Alquiler', expenses='0', rooms='2', bathrooms='2', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Manantiales', zone='SurOeste', street='Av. Directorio', height='258', price='55000', currency='$US', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños... Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vulputate, augue quis consectetur tempus, tortor augue vestibulum velit, quis sagittis nibh ex a orci. In feugiat leo eu dolor faucibus, vel fringilla odio laoreet. Quisque non mattis mauris. Duis congue malesuada urna non tempor. Mauris metus erat, rhoncus vitae elementum nec, tincidunt ac libero. Mauris vel lorem aliquet, porttitor quam non, accumsan ante. Quisque elementum finibus metus vitae accumsan. Praesent pulvinar molestie risus sit amet scelerisque. Vestibulum est enim, lobortis in hendrerit at, auctor et mi. Curabitur aliquet massa nec orci tempus, ut consectetur leo suscipit. Maecenas semper feugiat augue vel dapibus. Etiam ut mi erat. Integer malesuada enim non purus tempus, at vehicula arcu euismod. Sed dui turpis, fringilla vitae felis id, auctor semper diam. Sed faucibus vulputate diam et imperdiet. Vestibulum ac lectus quis ipsum congue molestie et mattis magna. Quisque porta hendrerit mollis. Donec a euismod lectus, ut porttitor nisi. Aenean tempus, justo eget varius gravida, mi sem sollicitudin leo, ut aliquam enim sem sit amet augue. Maecenas blandit erat sit amet mi vehicula luctus sit amet quis urna. Aenean sit amet molestie nisl. Ut consequat ex ante.', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=7, title='CASA CERCA DE PASEO ARTESANOS', walink='', type='Casa', operation='Alquiler', expenses='0', rooms='3', bathrooms='2', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Güemes', zone='SurOeste', street='Av. Alvarez', height='258', price='100000', currency='$ARS', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños... Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vulputate, augue quis consectetur tempus, tortor augue vestibulum velit, quis sagittis nibh ex a orci. In feugiat leo eu dolor faucibus, vel fringilla odio laoreet. Quisque non mattis mauris. Duis congue malesuada urna non tempor. Mauris metus erat, rhoncus vitae elementum nec, tincidunt ac libero. Mauris vel lorem aliquet, porttitor quam non, accumsan ante. Quisque elementum finibus metus vitae accumsan. Praesent pulvinar molestie risus sit amet scelerisque. Vestibulum est enim, lobortis in hendrerit at, auctor et mi. Curabitur aliquet massa nec orci tempus, ut consectetur leo suscipit. Maecenas semper feugiat augue vel dapibus. Etiam ut mi erat. Integer malesuada enim non purus tempus, at vehicula arcu euismod. Sed dui turpis, fringilla vitae felis id, auctor semper diam. Sed faucibus vulputate diam et imperdiet. Vestibulum ac lectus quis ipsum congue molestie et mattis magna. Quisque porta hendrerit mollis. Donec a euismod lectus, ut porttitor nisi. Aenean tempus, justo eget varius gravida, mi sem sollicitudin leo, ut aliquam enim sem sit amet augue. Maecenas blandit erat sit amet mi vehicula luctus sit amet quis urna. Aenean sit amet molestie nisl. Ut consequat ex ante.', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
    House(id=8, title='TERRENO EN GÜEMES', walink='', type='Terreno', operation='Alquiler', expenses='0', rooms='4', bathrooms='3', toilettes='1', garages='2', coveredGarage='Sí', pool='Sí', grill='Sí', floors='2', new='No', antique='2 años', surface='150m²', coveredSurface='129m²', city='Güemes', zone='SurOeste', street='Av. Matanza', height='258', price='145000', currency='$ARS', paymentMethods='Contado', description='Este duplex cuenta con 3 habitaciones, 2 baños... Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vulputate, augue quis consectetur tempus, tortor augue vestibulum velit, quis sagittis nibh ex a orci. In feugiat leo eu dolor faucibus, vel fringilla odio laoreet. Quisque non mattis mauris. Duis congue malesuada urna non tempor. Mauris metus erat, rhoncus vitae elementum nec, tincidunt ac libero. Mauris vel lorem aliquet, porttitor quam non, accumsan ante. Quisque elementum finibus metus vitae accumsan. Praesent pulvinar molestie risus sit amet scelerisque. Vestibulum est enim, lobortis in hendrerit at, auctor et mi. Curabitur aliquet massa nec orci tempus, ut consectetur leo suscipit. Maecenas semper feugiat augue vel dapibus. Etiam ut mi erat. Integer malesuada enim non purus tempus, at vehicula arcu euismod. Sed dui turpis, fringilla vitae felis id, auctor semper diam. Sed faucibus vulputate diam et imperdiet. Vestibulum ac lectus quis ipsum congue molestie et mattis magna. Quisque porta hendrerit mollis. Donec a euismod lectus, ut porttitor nisi. Aenean tempus, justo eget varius gravida, mi sem sollicitudin leo, ut aliquam enim sem sit amet augue. Maecenas blandit erat sit amet mi vehicula luctus sit amet quis urna. Aenean sit amet molestie nisl. Ut consequat ex ante.', img=['https://definicion.de/wp-content/uploads/2011/01/casa-2.jpg', 'https://content.arquitecturaydiseno.es/medio/2021/03/07/salon-de-una-casa-en-los-angeles-de-color-blanco_9a9d7a58_2000x1350.jpg', 'https://www.viacelere.com/wp-content/uploads/2024/05/decoracion-patio_destacada.jpg']),
]

# GET - Obtener todas las casas
@app.get("/houses", response_model=List[House])
def get_houses():
    return houses

# GET - Obtener una casa específica por ID
@app.get("/houses/{house_id}", response_model=House)
def get_house(house_id: int):
    house = next((h for h in houses if h.id == house_id), None)
    if house is None:
        raise HTTPException(status_code=404, detail="House not found")
    return house

# POST - Crear una nueva casa
@app.post("/houses", response_model=House, status_code=status.HTTP_201_CREATED)
def create_house(house: House):
    houses.append(house)
    return house

# PUT - Actualizar una casa existente
@app.put("/houses/{house_id}", response_model=House)
def update_house(house_id: int, updated_house: House):
    for idx, h in enumerate(houses):
        if h.id == house_id:
            houses[idx] = updated_house
            return updated_house
    raise HTTPException(status_code=404, detail="House not found")

# DELETE - Eliminar una casa
@app.delete("/houses/{house_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_house(house_id: int):
    global houses
    houses = [h for h in houses if h.id != house_id]
    return {"message": "House deleted successfully"}
