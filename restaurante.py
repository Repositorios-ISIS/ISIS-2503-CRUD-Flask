# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:12:02 2021

@author: user
"""

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship

class Restaurante():
    __tablename__ = 'restaurante_restaurante'
    id        = Column(Integer, primary_key= True)
    nombre    = Column(String(50))
    clave     = Column(String(50))
    cuenta    = Column(String(50))
    direccion = Column(String(50))
    productos = relationship('Producto',backref="owner")

    def __init__(self, nombre, clave, cuenta, direccion):
        self.nombre = nombre
        self.clave = clave
        self.cuenta = cuenta
        self.direccion = direccion

    def __str__(self):
        return '%s %s' % (self.direccion, self.cuenta)
        return '{}'.format(self.nombre)

