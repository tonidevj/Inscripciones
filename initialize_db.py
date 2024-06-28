from hora import db, create_app
# Importa la base de datos y la función create_app desde el módulo 'hora'
from hora.models import Carrera, Semestres
# Importa los modelos Carrera y Semestres desde el módulo 'hora.models'

app = create_app()
# Crea una instancia de la aplicación llamando a la función create_app()

with app.app_context():
    # Crea un contexto de aplicación para trabajar con la base de datos
    db.create_all()
    # Crea todas las tablas en la base de datos según los modelos definidos
    
    carrera1 = Carrera(name="Ingeniería de Sistemas")
    # Crea una instancia del modelo Carrera con el nombre "Ingeniería de Sistemas"
    carrera2 = Carrera(name="Ingeniería Civil")
    # Crea una instancia del modelo Carrera con el nombre "Ingeniería Civil"
    db.session.add(carrera1)
    # Añade la instancia carrera1 a la sesión de la base de datos
    db.session.add(carrera2)
    # Añade la instancia carrera2 a la sesión de la base de datos
    
    semestre1 = Semestres(name="Primer Semestre")
    # Crea una instancia del modelo Semestres con el nombre "Primer Semestre"
    semestre2 = Semestres(name="Segundo Semestre")
    # Crea una instancia del modelo Semestres con el nombre "Segundo Semestre"
    db.session.add(semestre1)
    # Añade la instancia semestre1 a la sesión de la base de datos
    db.session.add(semestre2)
    # Añade la instancia semestre2 a la sesión de la base de datos
    
    db.session.commit()
    # Confirma (commits) todos los cambios realizados en la sesión a la base de datos
