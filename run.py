from hora import create_app, db
# Importa la función create_app y la base de datos db desde el módulo (o carpeta) 'hora'

if __name__ == '__main__':
    # Comprueba si el archivo se está ejecutando directamente (no importado como módulo)
    app = create_app()
    # Crea una instancia de la aplicación llamando a la función create_app()
    app.run()
    # Ejecuta la aplicación. Esto solo se ejecutará si el archivo es ejecutado directamente.

with app.app_context():
    # Crea un contexto de aplicación para trabajar con la base de datos
    db.create_all()
    # Crea todas las tablas en la base de datos según los modelos definidos
