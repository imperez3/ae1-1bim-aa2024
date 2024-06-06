from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import Restaurant
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

# se crea un objetos de tipo Restaurant
Restaurant1 = Restaurant(NombreRestaurant="Mi Delicia", Ubicacion="La Magdalena", TipoLocal="Comida Rapida", CantMesas=10)
Restaurant2 = Restaurant(NombreRestaurant="La Sazon de Ivan", Ubicacion="Mitad del Mundo", TipoLocal="Bufette", CantMesas=25)
Restaurant3 = Restaurant(NombreRestaurant="Los Antojitos de La UTPL", Ubicacion="Centro de Loja", TipoLocal="Comida Rapida", CantMesas=15)

# se agrega los objetos de tipo Restaurant a la sesión
# a la espera de un commit
session.add(Restaurant1)
session.add(Restaurant2)
session.add(Restaurant3)

# se crea un objetos de tipo CentroDeportivo
CentroDeportivo1 = CentroDeportivo(NombreCentroDeportivo="Mi Alto Rendimiento Volley", Ubicacion="Carcelen", TiposDeporte="Volley Vall", CantAsistentes=100)
CentroDeportivo2 = CentroDeportivo(NombreCentroDeportivo="Mi Alto Rendimiento Futbol", Ubicacion="El Batan", TiposDeporte="Futbol", CantAsistentes=500)
CentroDeportivo3 = CentroDeportivo(NombreCentroDeportivo="Mi Alto Rendimiento Basket", Ubicacion="Quicentro Sur", TiposDeporte="Basket", CantAsistentes=500)

# se agrega los objetos de tipo CentroDeportivo a la sesión
# a la espera de un commit
session.add(CentroDeportivo1)
session.add(CentroDeportivo2)
session.add(CentroDeportivo3)

# se necesita confirmar los cambios que existan en la sessión
# se usar commit
session.commit()
