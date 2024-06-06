"""
    Agregar información en una colección de MongoDB
    desde Python
"""

from enlace_base import Caso

# se obtiene la colección general (base de datos)

db = Caso.Base_Datos
coleccion = db.Coneccion

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento
data_01 = {"NombreRestaurant":"Mi Delicia", "Ubicacion":"La Magdalena", "TipoLocal":"Comida Rapida", "CantMesas":10}


coleccion.insert_one(data_01)

# proceso que agrega una lista de documentos
lista = [
{"NombreRestaurant":"La Sazon de Ivan", "Ubicacion":"Mitad del Mundo", "TipoLocal":"Bufette", "CantMesas":25},
]

coleccion.insert_many(lista)
