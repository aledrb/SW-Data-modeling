import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Usuario(Base): 
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombredeusuario = Column(String(120), unique=True)
    clave = Column(String(120), unique=True)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id_fav = Column(Integer, primary_key=True)
    planetas_fav = Column(String(255), nullable=False)
    personajes_fav = Column(String(255), nullable=False)
    vehiculos_fav = Column(String(255), nullable=False)
    idusuario = Column(Integer, ForeignKey('usuario.id'))
    usuariofavoritos =  relationship(Usuario)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    universo = Column(Integer, ForeignKey('planetas.id'))
    favoritos = Column(Integer, ForeignKey('favoritos.personajes_fav'))
    usuario = relationship(Usuario)


class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    personajes = Column(Integer, ForeignKey('personajes.id'))
    densidad = Column(Integer)
    gravedad = Column(Integer)
    favoritos = Column(Integer, ForeignKey('favoritos.planetas_fav'))
    usuario = relationship(Usuario)


class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    modelo = Column(String(120), nullable=False)
    nombre = Column(String(120), nullable=False)
    fabricante = Column(String(120), nullable=False)
    pilotos = Column(Integer, ForeignKey('personajes.id'))
    favoritos = Column(Integer, ForeignKey('favoritos.vehiculos_fav'))
    usuario = relationship(Usuario)






    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')