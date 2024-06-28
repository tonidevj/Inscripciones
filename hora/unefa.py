from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import Semestres, User
from hora import db
from hora.auth import loggin_required

bp = Blueprint('unefa', __name__, url_prefix='/unefa')
# Crea un Blueprint llamado 'unefa' con el prefijo de URL '/unefa'

@bp.route('/campus', methods=['GET', 'POST'])
@loggin_required
# Define una ruta para '/campus' que acepta métodos GET y POST y requiere autenticación
def campus():
    if request.method == 'POST':
        # Comprueba si la solicitud es de tipo POST
        semestre_id = request.form.get('semestre')
        # Obtiene el semestre enviado en el formulario
        user_id = session.get('user_id')
        # Obtiene el ID del usuario de la sesión
        user = User.query.get(user_id)
        # Busca al usuario en la base de datos por su ID
        user.semestre_id = semestre_id
        # Asigna el semestre seleccionado al usuario
        db.session.commit()
        # Guarda los cambios en la base de datos
        return redirect(url_for('unefa.list_mat'))
        # Redirige a la vista 'list_mat'
    semestres = Semestres.query.all()
    # Obtiene todos los semestres de la base de datos
    return render_template('unefa/index.html', semestres=semestres)
    # Renderiza la plantilla 'index.html' pasando los semestres

@bp.route('/listMat')
def list_mat():
    return ""



# @bp.route('select-semester', methods['GET', 'POST'])
# # @bp.route('/Materiaslist')
# # def index():
# #     return "listas de carreras"

#yaaaaaaaaaaaaaaaaaaaaaaaaa