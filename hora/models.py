from hora import db
# Este será un modelo de la base de datos

# La clase User representa el nombre de la tabla en la base de datos
class User(db.Model):
    # Cada atributo representa una columna en la base de datos

    # 'id' contiene números enteros y es una clave primaria
    id = db.Column(db.Integer, primary_key=True)
    # 'username' es de tipo string, contiene un valor único y no acepta valores nulos
    username = db.Column(db.String(20), unique=True, nullable=False)
    # 'password' será un campo de tipo texto y no acepta valores nulos
    password = db.Column(db.Text, nullable=False)
    # 'carrera_id' es una clave foránea que hace referencia a la columna 'id' en la tabla 'carrera'
    carrera_id = db.Column(db.Integer, db.ForeignKey('carrera.id'), nullable=True)
    # 'semestre_id' es una clave foránea que hace referencia a la columna 'id' en la tabla 'semestres'
    semestre_id = db.Column(db.Integer, db.ForeignKey('semestres.id'), nullable=True)

    # Creamos un constructor
    # Esto es para manipular los datos y crear el objeto de la clase User
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    # Para representar los usuarios
    # Esto será para obtener los datos
    def __repr__(self):
        return f'<User: {self.username}>'

# Añadimos los modelos para carreras y semestres

class Carrera(db.Model):
    # 'id' contiene números enteros y es una clave primaria
    id = db.Column(db.Integer, primary_key=True)
    # 'name' es de tipo string, contiene un valor único y no acepta valores nulos
    name = db.Column(db.String(50), unique=True, nullable=False)
    # Relación uno a muchos con la clase User
    users = db.relationship('User', backref='carrera', lazy=True)


class Semestres(db.Model):
    # 'id' contiene números enteros y es una clave primaria
    id = db.Column(db.Integer, primary_key=True)
    # 'name' es de tipo string, contiene un valor único y no acepta valores nulos
    name = db.Column(db.String(50), unique=True, nullable=False)
    # Relación uno a muchos con la clase User
    users = db.relationship('User', backref='semestre', lazy=True) 

# Añadimos el modelo para materias

class Materias(db.Model):
    # 'id' contiene números enteros y es una clave primaria
    id = db.Column(db.Integer, primary_key=True)
    # 'materias_by' es una clave foránea que hace referencia a la columna 'id' en la tabla 'user'
    materias_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # 'title' es de tipo string, contiene un valor único y no acepta valores nulos
    title = db.Column(db.String(200), unique=True, nullable=False)
    # 'desc' será un campo de tipo texto y no acepta valores nulos
    desc = db.Column(db.Text, nullable=False)

    # Creamos un constructor
    # Esto es para manipular los datos y crear el objeto de la clase Materias
    def __init__(self, materias_by, title, desc):
        self.materias_by = materias_by
        self.title = title
        self.desc = desc

    # Para representar las materias
    # Esto será para obtener los datos
    def __repr__(self):
        return f'<Materias: {self.title}>'

    # odio sqlalchemy
    