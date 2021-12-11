from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import db_session

import db_session

app = Flask(__name__)

engine = db_session.get_engine_from_settings()

"""
class Producto(db.Model):
    __tablename__ = 'producto_producto'
    id_prod     = db.Column(db.Integer, primary_key= True)
    nombre      = db.Column(db.String(50))
    precio      = db.Column(db.Float)
    informacion = db.Column(db.String(50))
    owner_id    = db.Column(db.Integer, db.ForeignKey('restaurante.id'))

    def __init__(self, nombre, clave, cuenta, direccion):
        self.id_prod     = id_prod
        self.nombre      = nombre
        self.precio      = precio
        self.informacion = informacion
        self.owner_id    = owner_id

    def __str__(self):
        return '%s %s' % (self.nombre, self.precio)
        return '{}'.format(self.informacion)
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_restaurante", methods=['POST'])
def add_restaurante():
    if request.method == 'POST':
        nombre      = request.form['nombre']
        clave       = request.form['clave']
        cuenta      = request.form['cuenta']
        direccion   = request.form['direccion']
        
        x=None
        
        with engine.connect() as con:
            data = {"nombre":nombre,'clave':clave,"cuenta":cuenta,"direccion":direccion}
            statement = text("INSERT INTO restaurante_restaurante(nombre, clave, cuenta, direccion) VALUES (:nombre, :clave, :cuenta, :direccion)")
            x = engine.execute(statement,**data)
        
        return f"Restaurante {nombre} creado"


@app.route("/get_something")
def who():
    rs = "a"
    #inspector = inspect(engine)
    #return inspector.get_columns('restaurante_restaurante')
    return rs


@app.route("/hi/<username>")
def greet(username):
    return f"hi there, {username}!"

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
