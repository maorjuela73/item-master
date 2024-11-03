from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import unittest

engine = create_engine('sqlite:///item_master.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    contenido = Column(String, nullable=False)
    dificultad = Column(Float, nullable=False)      # Parámetro a
    discriminacion = Column(Float, nullable=False)  # Parámetro b
    adivinacion = Column(Float, nullable=False)     # Parámetro c

    # Relación con las opciones de respuesta
    opciones = relationship("OpcionDeRespuesta", back_populates="item", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Item(id={self.id}, contenido='{self.contenido}')>"

class OpcionDeRespuesta(Base):
    __tablename__ = 'opciones_de_respuesta'

    id = Column(Integer, primary_key=True)
    clave = Column(String, nullable=False)
    es_correcta = Column(Boolean, nullable=False)  # True si es la respuesta correcta
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)

    # Relación inversa hacia el ítem
    item = relationship("Item", back_populates="opciones")

    def crear_opcion(self, item_id, clave, es_correcta):
        nueva_opcion = OpcionDeRespuesta(
            item_id=item_id,
            clave=clave,
            es_correcta=es_correcta
        )
        session.add(nueva_opcion)
        session.commit()
        return nueva_opcion

    def __repr__(self):
        return f"<OpcionDeRespuesta(id={self.id}, clave='{self.clave}', es_correcta={self.es_correcta})>"

class Evaluador(Base):
    __tablename__ = 'evaluadores'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def crear_item(self, contenido, dificultad, discriminacion, adivinacion):
        nuevo_item = Item(
            contenido=contenido,
            dificultad=dificultad,
            discriminacion=discriminacion,
            adivinacion=adivinacion
        )
        session.add(nuevo_item)
        session.commit()
        return nuevo_item

    def editar_item(self, item_id, **kwargs):
        item = session.query(Item).filter_by(id=item_id).first()
        if item:
            for key, value in kwargs.items():
                setattr(item, key, value)
            session.commit()
            return item
        else:
            return None

    def eliminar_item(self, item_id):
        item = session.query(Item).filter_by(id=item_id).first()
        if item:
            session.delete(item)
            session.commit()
            return True
        else:
            return False

    def __repr__(self):
        return f"<Evaluador(nombre='{self.nombre}', email='{self.email}')>"

class Evaluado(Base):
    __tablename__ = 'evaluados'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Evaluado(nombre='{self.nombre}', email='{self.email}')>"

Base.metadata.create_all(engine)

# Cargar items de csv
import csv

with open('items.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        item = Item(
            contenido=row['contenido'],
            dificultad=float(row['dificultad']),
            discriminacion=float(row['discriminacion']),
            adivinacion=float(row['adivinacion'])
        )
        session.add(item)

    session.commit()

with open('opciones_items.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        opcion = OpcionDeRespuesta(
            clave=row['clave'],
            es_correcta=row['es_correcta'] == 'True',
            item_id=int(row['item_id'])
        )
        session.add(opcion)
    session.commit()


# Cerrar la sesión
session.close()


print("Done!")