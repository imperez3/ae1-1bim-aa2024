"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import Caso

# se obtiene la colección general (base de datos)

db = Caso.Base_Datos
coleccion = db.Coneccion

# se usa método find_one, a partir de la colección
print("Muestra un solo documento de la base de datos")
data_01 = coleccion.find_one()
print(data_01)

# se usa método find, a partir de la colección
print("Muestra todos los documentos de la base de datos")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)
