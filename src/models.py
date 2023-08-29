from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diametro = db.Column(db.String(120), unique=True, nullable=False)
    nombre = db.Column(db.String(80), unique=False, nullable=False)
    clima = db.Column(db.String(80), unique=False, nullable=False)
    gravedad = db.Column(db.String(80), unique=False, nullable=False)
    poblacion = db.Column(db.String(80), unique=False, nullable=False)
    


    def __repr__(self):
        return '<Planets %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "diametro": self.diametro,
            "nombre": self.nombre,
            "clima": self.clima,
            "gravedad": self.gravedad,
            "poblacion": self.poblacion,
            # do not serialize the password, its a security breach


        }
class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    genero= db.Column(db.String(80), unique=False, nullable=False)
    color_de_pelo = db.Column(db.String(80), unique=False, nullable=False)
    especie = db.Column(db.String(80), unique=False, nullable=False)
    color_de_ojos = db.Column(db.String(80), unique=False, nullable=False)
    


    def __repr__(self):
        return '<Personajes %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "color_de_pelo": self.color_de_pelo,
            "especie": self.especie,
            "color_de_ojos": self.diametro,
 }


class Vehiculos(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    manufacturer   = db.Column(db.String(120), unique=True, nullable=False)
    cost_in_credits   = db.Column(db.String(80), unique=False, nullable=False)
    length   = db.Column(db.String(80), unique=False, nullable=False)
    crew   = db.Column(db.String(80), unique=False, nullable=False)
    passengers   = db.Column(db.String(80), unique=False, nullable=False)
        


    def __repr__(self):
        return '<Vehiculos %r>' % self.manufacturer

    def serialize(self):
        return {
            "id": self.id,
            "cost_in_credits": self.cost_in_credits,
            "length ": self.length ,
            "manufacturer": self.manufacturer,
            "crew ": self.crew ,
            "passengers ": self.passengers ,
             }


class Favoritos(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    user_id  = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = relationship(User)
#  user_id  = db.Column(db.Integer, db.ForeignKey("user.id"))
#  user_id  = db.Column(db.Integer, db.ForeignKey("user.id"))





    



            
