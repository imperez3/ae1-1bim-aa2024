from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import CentroDeportivo
# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,
# desde el generador de clases de SQLAlchemy
# sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session
# de tipo Session, que permite: permitir guardar, eliminar,
# actualizar y generar consultas a la base de datos.
session = Session()

# Obtener todos los registros de la entidad Autor con una(s) condición.
# Se hace uso del método query.
# filter, permite agregrar condiciones a la búsqueda, con base
# a las propiedades de la entidad
lista_Centro = session.query(CentroDeportivo).filter(CentroDeportivo.Ubicacion=="Carcelen")
# La variable lista_Centro, tendrá un listado de objetos de tipo CentroDeportivo que
# tengan en la propiedad de Ubicacion el valor: Carcelen

# se realiza un proceso iterativo para presentar la información
# de cada objeto.
for l in lista_Centro:
    print(l)
