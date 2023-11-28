import sqlite3

# Primero hay que crear la conección a la Base de datos
conexion = sqlite3.connect("Blog-Python-colaborativo/Ejemplo sin POO/sinPOO.sqlite")

# Crear el cursor que se encarga de las tareas
cursor = conexion.cursor()
# Puede llamarse como se quiera, hasta nombre propio jaja

# Código para crear la tabla "posteos" si no existe
text = """CREATE TABLE IF NOT EXISTS posteos (
        idPost INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo,
        contenido,
        autor,
        fecha,
        imagen,
        tags
        );
        """

# Ejecuta la tarea
cursor.execute(text)

# Guarda la ejecución de la mimsa (para que no se pierda)
conexion.commit()

# Función para crear un artículo
def crearArticulo(titulo,contenido,autor,fecha,imagen,tags):
    articulo={}
    articulo["titulo"]=titulo
    articulo["contenido"]=contenido
    articulo["autor"]=autor
    articulo["fecha"]=fecha
    articulo["imagen"]=imagen
    articulo["tags"]=tags
    return articulo

# Función para insertar un artículo en la base de datos
def insertar(articulo):
    global cursor
    text = """INSERT INTO posteos (titulo,contenido,autor,fecha,imagen,tags) VALUES  (?,?,?,?,?,?);"""
    data = (articulo["titulo"], articulo["contenido"],articulo["autor"],articulo["fecha"],articulo["imagen"],articulo["tags"])
    cursor.execute(text, data)

# Función para leer y mostrar todos los artículos
def leer():
    global cursor
    cursor.execute("""SELECT * FROM posteos""")
    elementos = cursor.fetchall()
    for post in elementos:
        print(post)

# Crear un artículo de ejemplo y guardarlo en la base de datos
art = crearArticulo("titulo","contenido","autor","fecha","imagen","tags")
insertar(art)

# Leer y mostrar todos los artículos de la base de datos
leer()

# Guardar los cambios en la base de datos y cerrar la conexión
conexion.commit()
conexion.close()