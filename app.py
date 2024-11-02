from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
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

    def __repr__(self):
        return f"<Item(id={self.id}, contenido='{self.contenido}')>"

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

print("Done!")