from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
db = SQLAlchemy()


class User(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    email         = db.Column(db.String(120), unique=True, nullable=False)
    password      = db.Column(db.String(80), unique=False, nullable=False)
    is_active     = db.Column(db.Boolean(), unique=False, nullable=False)
    

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id":    self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id                 = db.Column(db.Integer, primary_key=True)
    diametro           = db.Column(db.String(120), unique=True, nullable=False)
    nombre             = db.Column(db.String(80), unique=False, nullable=False)
    clima              = db.Column(db.String(80), unique=False, nullable=False)
    gravedad           = db.Column(db.String(80), unique=False, nullable=False)
    poblacion          = db.Column(db.String(80), unique=False, nullable=False)
    


    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id":           self.id,
            "diametro":     self.diametro,
            "nombre":       self.nombre,
            "clima":        self.clima,
            "gravedad":     self.gravedad,
            "poblacion":    self.poblacion,
            # do not serialize the password, its a security breach
            "usuario_favoritos":list(map(lambda item: item.serialize(),self.usuario_favoritos))

        }
class Personajes(db.Model):
    id                 = db.Column(db.Integer, primary_key=True)
    nombre             = db.Column(db.String(120), unique=True, nullable=False)
    genero             = db.Column(db.String(80), unique=False, nullable=False)
    color_de_pelo      = db.Column(db.String(80), unique=False, nullable=False)
    especie            = db.Column(db.String(80), unique=False, nullable=False)
    color_de_ojos      = db.Column(db.String(80), unique=False, nullable=False)
    


    def __repr__(self):
        return '<Personajes %r>' % self.nombre

    def serialize(self):
        return {
            "id":            self.id,
            "nombre":        self.nombre,
            "genero":        self.genero,
            "color_de_pelo": self.color_de_pelo,
            "especie":       self.especie,
            "color_de_ojos": self.color_de_ojos,
 }


class Vehiculos(db.Model):
    id                    = db.Column(db.Integer, primary_key=True)
    manufacturer          = db.Column(db.String(120), unique=True, nullable=False)
    cost_in_credits       = db.Column(db.String(80), unique=False, nullable=False)
    length                = db.Column(db.String(80), unique=False, nullable=False)
    crew                  = db.Column(db.String(80), unique=False, nullable=False)
    passengers            = db.Column(db.String(80), unique=False, nullable=False)
        


    def __repr__(self):
        return '<Vehiculos %r>' % self.manufacturer

    def serialize(self):
        return {
            "id":                  self.id,
            "cost_in_credits":     self.cost_in_credits,
            "length ":             self.length ,
            "manufacturer":        self.manufacturer,
            "crew ":               self.crew ,
            "passengers ":         self.passengers ,
             }



class Naves(db.Model):
    id                = db.Column(db.Integer, primary_key=True)
    manufacturer      = db.Column(db.String(120), unique=True, nullable=False)
    cost_in_credits   = db.Column(db.String(80), unique=False, nullable=False)
    length            = db.Column(db.String(80), unique=False, nullable=False)
    crew              = db.Column(db.String(80), unique=False, nullable=False)
    passengers        = db.Column(db.String(80), unique=False, nullable=False)
    model             = db.Column(db.String(80), unique=False, nullable=False)

    
        
        


    def __repr__(self):
        return '<Vehiculos %r>' % self.manufacturer

    def serialize(self):
        return {
            "id":                 self.id,
            "cost_in_credits":    self.cost_in_credits,
            "length ":            self.length ,
            "manufacturer":       self.manufacturer,
            "crew ":              self.crew ,
            "passengers ":        self.passengers ,
             }


class Favoritos(db.Model):
    id                = db.Column(db.Integer, primary_key=True)
    user_id           = db.Column(db.Integer, db.ForeignKey("user.id"))
   
    personajes_id     = db.Column(db.Integer, db.ForeignKey("personajes.id"))
    planets_id        = db.Column(db.Integer, db.ForeignKey("planets.id"))
    vehiculos_id      = db.Column(db.Integer, db.ForeignKey("vehiculos.id"))
    naves_id          = db.Column(db.Integer, db.ForeignKey("naves.id"))


    planets =     db.relationship(Planets)
    personajes =  db.relationship(Personajes)
    naves =       db.relationship(Naves)
    user =        db.relationship(User)
    vehiculos =   db.relationship(Vehiculos)



    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        return {
            "id":                      self.id,
            "user_id":                 self.user_id,
           
            "personajes_id": None if self.personajes is None else self.personajes.serialize(),
           
            " planets_id": None if self. planets is None else self. planets.serialize(),
            
            "vehiculos _id": None if self. vehiculos is None else self. vehiculos.serialize(),
           
            "naves _id": None if self. naves is None else self. naves.serialize(),
           
             }




    



            
