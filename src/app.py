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
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Cambia a tu base de datos
# db = SQLAlchemy(app)
# admin = Admin(app)

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

# User

@app.route('/user', methods=['GET'])
def get_users():

    users = User.query.all()
    users= list(map(lambda user : user.serialize(),users))
    return { 'msj' : 'no hay usuarios'}, 404
    return jsonify(users), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    user = user.serialize()
    return jsonify(user), 200






# Planetas


@app.route('/planetas', methods=['GET'])
def handle_planetas():

    allplanetas = Planets.query.all()
    planetasList = list(map(lambda p: p.serialize(),allplanetas))

    if planetasList == []:
        return { 'msj' : 'no hay planetas'}, 404
    
    return jsonify(planetasList), 200

@app.route('/planeta/<int:planeta_id>', methods=['GET'])
def un_planeta(planets_id):

    unplaneta =Planets.query.filter_by(id=planets_id).first()

    if unplaneta is None:
        return { 'msj' : 'no existe'}, 404


    return jsonify( unplaneta.serialize()), 200


@app.route('/planeta', methods=['POST'])
def crear_un_planeta():
    body = json.loads(request.data)
    nuevo_planeta = Planets(
        diametro = body["diametro"],
        nombre = body["nombre"],
        clima = body["clima"],
        gravedad = body["gravedad"],
        poblacion = body["poblacion"]
    )
    db.session.add(nuevo_planeta)
    db.session.commit()
    
    return jsonify(nuevo_planeta.serialize()), 200
        


    
# Personajes


@app.route('/personajes', methods=['GET'])
def handle_personajes():

    allpersonajes = Personajes.query.all()
    personajesList = list(map(lambda personajes: personajes.serialize(),allpersonajes))
    return jsonify(personajesList),200




@app.route('/personajes/<int:personajes_id>', methods=['GET'])
def un_personajes(personaje_id):

    unpersonajes = Personajes.query.filter_by(id=personaje_id).first()

    if unpersonajes is None:
        return { 'msj' : 'no existe'}, 404


    return jsonify( unpersonajes.serialize()), 200


@app.route('/personajes/<int:personajes_id>', methods=['DELETE'])
def delete_personajes(personajes_id):

    personajes = Personajes.query.filter_by(id=personajes_id).first()
    if personajes:
        db.session.delete(personajes)
        db.session.commit()
        return jsonify({"msj":"Personajes DELETED"}), 200
    
    return { 'msj' : 'no hay personajes'}, 404

    # return jsonify(personajesList),200
        


@app.route('/personajes', methods=['POST'])
def create_personaje():
    request_body = json.loads(request.data)

    existing_personaje = Personajes.query.filter_by(**request_body).first()

    if existing_personaje:
        return jsonify({"msj": "El personaje ya existe"}), 400

    new_personaje = Personajes(**request_body)
    db.session.add(new_personaje)
    db.session.commit()
    
    return jsonify(new_personaje.serialize()), 200
        
    

    
# Vehiculos

    
# @app.route('/vehiculos', methods=['GET'])
# def get_vehiculos():

#     allvehiculos = vehiculos.query.all()
#     allvehiculos = list(map(lambda vehiculos: vehiculos.serialize(),vehiculos))

#     return jsonify(vehiculos), 200

# @app.route('/vehiculos/<int:vehiculos_id>', methods=['GET'])
# def get_vehiculos_id(vehiculos_id):

#     vehiculo = vehiculos.query.get(vehiculos_id)
#     vehiculo = vehiculos.serialize()

    return jsonify(vehiculo), 200

@app.route('/vehiculos/<int:id>', methods=['DELETE'])
def delete_vehiculos(id):
    vehiculos = vehiculos.query.get(id)
    vehiculos.delete()
    return jsonify({ "message": "Vehiculos DELETED" }), 200







    unvehiculos = Vehiculos.query.filter_by(id=vehiculos_id).first()

    if unvehiculos is None:
        return { 'msj' : 'no existe'}, 404


   


#  @app.route('/vehiculos', methods=['POST'])
# def crear_un_vehiculo():
#     body = json.loads(request.data)

#     nuevo_vehiculo =Vehiculos(
#         manufacturer = body["manufacturer"],
#         cost_in_credits = body["cost_in_credits"],
#         length = body[" length "],
#          crew = body["crew"],
#         passengers = body["passengers"]
#     )
#     db.session.add(nuevo_vehiculo)
#     db.session.commit()
    
#     return jsonify({"msg":"planeta agregado con exito"}), 200
        
        
# Naves

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



@app.route('/naves', methods=['POST'])
def crear_un_naves():
    body = json.loads(request.data)
    nuevo_naves = Planets(
        manufacturer = body["manufacturer"],
        cost_in_credits = body["cost_in_credits"],
        length = body[" length "],
         crew = body["crew"],
        passengers = body["passengers"]
    )
    db.session.add(nuevo_naves)
    db.session.commit()
    
    return jsonify({"msj":"nave agregado con exito"}), 200





    

# Favoritos

@app.route('/favoritos', methods=['GET'])
def get_favoritos():
    favoritos = Favoritos.query.all()
    favoritos = list(map(lambda favoritos: favoritos.serialize(), favoritos))
    if favoritos == [] :
        return ({ "msj": "no hay usuario" }), 404
    return favoritos, 200


@app.route('/favoritos/<int:id>', methods=['GET'])
def select_fav(id):
    favoritos = Favoritos.query.filter_by(user_id = id).all()
    favoritos_user = [favoritos.serialize() for favoritos in favoritos]
    return jsonify(favoritos_user), 200

@app.route('/favoritos', methods=['POST'])
def new_favoritos():  
    
    datos = request.get_json()
    favoritos = Favoritos()
    favoritos.user_id = datos['user_id']
    favoritos.people_id = datos['personajes_id']
    favoritos.planet_id = datos['planet_id']
    favoritos.vehiculos_id = datos['vehiculos_id']
    favoritos.vaves_id = datos['naves_id']
    favoritos.save()
    return jsonify(favoritos.serialize()), 201

@app.route('/favorite/people', methods=['POST'])
def new_favoritepeople(): 
    datos = request.get_json()
    favoritos = Favoritos()
    favoritos.user_id = datos['user_id']
    favoritos.people_id = datos['people_id']
    favoritos.save()
    return jsonify(favoritos.serialize()), 201

@app.route('/favoritos/planet', methods=['POST'])
def new_favoritosplanet(): 
    datos = request.get_json()
    favoritos = Favoritos()
    favoritos.user_id = datos['user_id']
    favoritos.planet_id = datos['planet_id']
    favoritos.save()
    return jsonify(favoritos.serialize()), 201

@app.route('/favoritos/naves', methods=['POST'])
def new_favoritosnaves(): 
    datos = request.get_json()
    favoritos = Favoritos()
    favoritos.user_id = datos['user_id']
    favoritos.naves_id = datos['naves_id']
    favoritos.save()
    return jsonify(favoritos.serialize()), 201
   
@app.route('/favoritos/<int:user_id>/planet/<int:planet_id>', methods=['DELETE'])
def delete_favoritosplanet(planet_id, user_id):
    favorito = Favoritos.query.filter_by(planet_id=planet_id,user_id=user_id).first()
    if favorito: 
        db.session.delete(favorito)
        db.session.commit()
        return jsonify({ "msj": "FavPlanet DELETED" }), 200

@app.route('/favoritos/<int:user_id>/personajes/<int:personaje_id>', methods=['DELETE'])
def delete_favoritospersonajes(user_id, id):
    favoritos = Favoritos.query.filter_by(personajes_id =id,user_id =user_id).first()
    if favoritos:
        db.session.delete(favoritos)
        db.session.commit()
        return jsonify({ "msj": "personajes DELETED" }), 200

@app.route('/favoritos/naves/<int:id>', methods=['DELETE'])
def delete_favoritosnaves(id):
    favoritos = Favoritos.query.filter_by(naves_id = id).first()
    favoritos.delete()
    return jsonify({ "msj": "naves DELETED" }), 200
## ALL Favorites



# this only runs if `$ python src/app.py` is executed
if __name__ == '_main_':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)






