from flask import Blueprint, render_template, request, redirect, url_for, session, flash, g
# Importa módulos de Flask para manejar rutas, plantillas, solicitudes, redirecciones, URLs, sesiones, mensajes flash y contexto global 'g'
from werkzeug.security import generate_password_hash, check_password_hash
# Importa funciones de Werkzeug para generar y verificar hashes de contraseñas
from .models import User
# Importa el modelo User desde el paquete actual
from hora import db
# Importa la base de datos desde el módulo 'hora'

# Crea un Blueprint llamado 'auth' con el prefijo de URL '/auth'
bp = Blueprint('auth', __name__, url_prefix='/auth')

# Ruta para registrar nuevos usuarios
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Crea un nuevo usuario con el nombre de usuario y la contraseña proporcionados
        user = User(username=username, password=generate_password_hash(password))

        # Verifica si ya existe un usuario con el mismo nombre de usuario
        user_name = User.query.filter_by(username=username).first()
        if user_name is None:
            # Si no existe, añade el nuevo usuario a la base de datos
            db.session.add(user)
            db.session.commit()
            # Redirige al usuario a la página de inicio de sesión
            return redirect(url_for('auth.login'))
        else:
            error = f'El usuario {username} ya existe'
            flash(error)  # Muestra un mensaje de error
    return render_template('auth/register.html')  # Renderiza la plantilla de registro

# Ruta para iniciar sesión
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None
        # Busca al usuario en la base de datos por su nombre de usuario
        user = User.query.filter_by(username=username).first()
        if user is None:
            error = 'Nombre de usuario incorrecto'
        elif not check_password_hash(user.password, password):
            error = 'Clave inválida'
        
        if error is None:
            # Si no hay errores, establece la sesión para el usuario autenticado
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('unefa.campus'))  # Redirige al usuario a la página principal después del inicio de sesión
        
        flash(error)  # Muestra un mensaje de error si la autenticación falla

    return render_template('auth/login.html')  # Renderiza la plantilla de inicio de sesión

# Función ejecutada antes de cualquier solicitud a la aplicación
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

# Ruta para cerrar sesión
@bp.route('/logout')
def logout():
    session.clear()  # Limpia la sesión (cierra sesión)
    return redirect(url_for('index'))  # Redirige al usuario a la página de inicio

import functools

# Decorador para requerir autenticación
def loggin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))  # Redirige al usuario a la página de inicio de sesión si no está autenticado
        return view(**kwargs)
    return wrapped_view
