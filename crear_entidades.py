from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column, Integer, String
# se importa el engine
from base_datos import engine

# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
Base = declarative_base()

# Se crea la una entidad llamada Autor, que hereda
# de Base
class Restaurant(Base):
    __tablename__ = 'Restaurant' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    NombreRestaurant = Column(String) # atributo de tipo String
    Ubicacion = Column(String)
    TipoLocal = Column(String)
    CantMesas = Column(Integer)

    def __str__(self):
        return "%s %s %s %s" % (self.NombreRestaurant, self.Ubicacion, self.TipoLocal,
        self.CantMesas)
    

#crear clase o entidad centros deportivos
class CentroDeportivo(Base):
    __tablename__ = 'CentroDeportivo' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    NombreCentroDeportivo = Column(String) # atributo de tipo String
    Ubicacion = Column(String)
    TiposDeporte = Column(String)
    CantAsistentes = Column(Integer)

    def __str__(self):
        return "%s %s %s %s" % (self.NombreCentroDeportivo, self.Ubicacion, self.TiposDeporte,
        self.CantAsistentes)
# Sentencia que permite crear o migrar las clases en Python al
# gestor de base de datos, expresado en el engine.
Base.metadata.create_all(engine)
