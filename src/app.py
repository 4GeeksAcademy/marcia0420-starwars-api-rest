"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Planets,Personajes,Vehiculos,Naves,Favoritos

#from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_user():

    allusuarios = User.query.all()
    usuariosList = list(map(lambda p: p.serialize(),allusuarios))

    if usuariosList == []:
        return { 'msj' : 'no hay usuarios'}, 404

    return jsonify(usuariosList), 200

   

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

"""-----------------------------------------------_<Planetas>_-------------------------------------"""


@app.route('/planetas', methods=['GET'])
def handle_planetas():

    allplanetas = Planets.query.all()
    planetasList = list(map(lambda p: p.serialize(),allplanetas))

    if planetasList == []:
        return { 'msj' : 'no hay planetas'}, 404
    
    return jsonify(planetasList), 200

@app.route('/planeta/<int:planeta_id>', methods=['GET'])
def un_planeta(planeta_id):

    unplaneta =Planets.query.filter_by(id=planeta_id).first()

    if unplaneta is None:
        return { 'msj' : 'no existe'}, 404


    return jsonify( unplaneta.serialize()), 200
        


    



    




    
    """-----------------------------------------------_<Personajes>_-------------------------------------"""


@app.route('/personajes', methods=['GET'])
def handle_personajes():

    allpersonajes = Personajes.query.all()
    personajesList = list(map(lambda p: p.serialize(),allpersonajes))

    if personajesList == []:
        return { 'msj' : 'no hay personajes'}, 404
    return jsonify(personajesList)
        
@app.route('/personajes/<int:personaje_id>', methods=['GET'])
def un_personaje(personaje_id):

    unpersonaje = Personajes.query.filter_by(id=personaje_id).first()

    if unpersonaje is None:
        return { 'msj' : 'no existe'}, 404


    return jsonify( unpersonaje.serialize()), 200
        
    

    
"""-----------------------------------------------_<Vehiculos>_-------------------------------------"""

@app.route('/vehiculos', methods=['GET'])
def handle_vehiculos():

    allvehiculos = Vehiculos.query.all()
    vehiculosList = list(map(lambda p: p.serialize(),allvehiculos))

    if vehiculosList == []:
        return { 'msj' : 'no hay vehiculos'}, 404
    
    return jsonify(vehiculosList), 200



    """-----------------------------------------------_<Naves>_-------------------------------------"""



    

@app.route('/naves', methods=['GET'])
def handle_naves():

    allnaves = Naves.query.all()
    navesList = list(map(lambda p: p.serialize(),allnaves))

    if navesList == []:
        return { 'msj' : 'no hay naves'}, 404


    return jsonify(navesList), 200



"""-----------------------------------------------_<Naves>_-------------------------------------"""
    