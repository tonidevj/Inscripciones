from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Inicialización de la instancia de SQLAlchemy
db = SQLAlchemy()

# Función para crear la aplicación Flask
def create_app():
    app = Flask(__name__)  # Crea una instancia de la aplicación Flask

    # Configuración de la aplicación
    app.config.from_mapping(
        DEBUG=True,  # Habilita el modo debug
        SECRET_KEY='dev',  # Clave secreta para sesiones y otros usos
        SQLALCHEMY_DATABASE_URI="sqlite:///materias.db"  # URI de la base de datos 
    )

    db.init_app(app)  # Inicializa la aplicación con SQLAlchemy

    # Importa y registra el Blueprint 'unefa'
    from . import unefa
    app.register_blueprint(unefa.bp)

    # Importa y registra el Blueprint 'auth'
    from . import auth
    app.register_blueprint(auth.bp)

    # Ruta principal que renderiza el template 'index.html'
    @app.route('/')
    def index():
        return render_template('index.html')

    # Crea todas las tablas en la base de datos al iniciar la aplicación
    with app.app_context():
        db.create_all()

    return app  # Retorna la aplicación Flask creada

