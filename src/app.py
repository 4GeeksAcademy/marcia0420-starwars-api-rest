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
import json

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



@app.route('/personajes', methods=['POST'])
def create_personaje():
    request_body = json.loads(request.data)

    existing_personaje = Personajes.query.filter_by(**request_body).first()

    if existing_personaje:
        return jsonify({"message": "El personaje ya existe"}), 400

    new_personaje = Personajes(**request_body)
    db.session.add(new_personaje)
    db.session.commit()
    
    return jsonify(new_personaje.serialize()), 200
        
    

    
"""-----------------------------------------------_<Vehiculos>_-------------------------------------"""

@app.route('/vehiculos', methods=['GET'])
def handle_vehiculos():

    allvehiculos = Vehiculos.query.all()
    vehiculosList = list(map(lambda p: p.serialize(),allvehiculos))

    if vehiculosList == []:
        return { 'msj' : 'no hay vehiculos'}, 404
    
    return jsonify(vehiculosList), 200




@app.route('/vehiculos/<int:vehiculos_id>', methods=['GET'])
def un_vehiculos(vehiculos_id):

    unvehiculos = Vehiculos.query.filter_by(id=vehiculos_id).first()

    if unvehiculos is None:
        return { 'msj' : 'no existe'}, 404


    return jsonify( unvehiculos.serialize()), 200



    """-----------------------------------------------_<Naves>_-------------------------------------"""



    

@app.route('/naves', methods=['GET'])
def handle_naves():

    allnaves = Naves.query.all()
    navesList = list(map(lambda p: p.serialize(),allnaves))

    if navesList == []:
        return { 'msj' : 'no hay naves'}, 404


    


@app.route('/naves/<int:naves_id>', methods=['GET'])
def un_naves(naves_id):

    unnaves = Naves.query.filter_by(id=naves_id).first()

    if unnaves is None:
        return { 'msj' : 'no existe'}, 404


    return jsonify( unnaves.serialize()), 200




"""-----------------------------------------------_<Naves>_-------------------------------------"""
    

"""-----------------------------------------------_<Favoritos>_-------------------------------------"""




@app.route('/favoritos', methods=['GET'])
def handle_():

    allfavoritos = Favoritos.query.all()
    favoritosList = list(map(lambda p: p.serialize(),allfavoritos))

    if favoritosList == []:
        return { 'msj' : 'no hay favoritos'}, 404
    return jsonify(favoritosList)
        
@app.route('/user/favoritos', methods=['GET'])
def un_favoritos():



# user_id =  get_user_id()
#    user_favoritos =favoritos.query.filter
#    user_favoritos = favoritos.query.filter.by_(user-id=user_id).all())
# serialized_favorites = [favorite.serialize() for favorite in user_favorites]
   
#  return jsonify(serialized_favorites)

    allfavoritos = Favoritos.query.all()
    favoritosList = list(map(lambda p: p.serialize(),allfavoritos))


    
if favoritosList == []:
    return { 'msj' : 'no existe'}, 404

return jsonify( un_favoritos.serialize()), 200



@app.route('/favoritos', methods=['POST'])
def create_favoritos():
    request_body = json.loads(request.data)

    existing_favoritos = Favoritos.query.filter_by(**request_body).first()

    if existing_favoritos:
        return jsonify({"message": "El favoritos ya existe"}), 400

    new_favoritos = Favoritos(**request_body)
    db.session.add(new_favoritos)
    db.session.commit()
    
    return jsonify(new_favoritos.serialize()), 200