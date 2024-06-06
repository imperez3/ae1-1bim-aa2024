"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import Caso

# se obtiene la colección general (base de datos)

db = Caso.Caso_Estudio
coleccion = db.Caso

# se usa método find_one con parámetros, a partir de la colección
print("Muestra un solo documento de la base de datos")
data_01 = coleccion.find_one({'NombreRestaurant':'Mi Delicia'})
print(data_01)

# se usa método find con parámetros, a partir de la colección
print("Muestra todos los documentos de la base de datos que cumplan con la \
condición")
data_02 = coleccion.find({'CantMesas':{"$lt":25}})
for registro in data_02:
    print(registro)
