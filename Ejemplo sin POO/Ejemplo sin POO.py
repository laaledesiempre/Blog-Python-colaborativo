import sqlite3




# Primero hay que crear la conección a la Base de datos
conexion = sqlite3.connect("Blog-Python-colaborativo/Ejemplo sin POO/sinPOO.sqlite")

# Crear el cursor que se encarga de las tareas
cursor = conexion.cursor()
# Puede llamarse como se quiera, hasta nombre propio jaja

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


def crearArticulo(titulo,contenido,autor,fecha,imagen,tags):
    articulo={}
    articulo["titulo"]=titulo
    articulo["contenido"]=contenido
    articulo["autor"]=autor
    articulo["fecha"]=fecha
    articulo["imagen"]=imagen
    articulo["tags"]=tags
    return articulo
    

def insertar(articulo):
    global cursor
    text = """INSERT INTO posteos (titulo,contenido,autor,fecha,imagen,tags) VALUES  (?,?,?,?,?,?);"""
    data = (articulo["titulo"], articulo["contenido"],articulo["autor"],articulo["fecha"],articulo["imagen"],articulo["tags"])

    cursor.execute(text, data)


    
def leer():
    global cursor
    cursor.execute("""SELECT * FROM posteos""")
    elementos = cursor.fetchall()
    for post in elementos:
        print(post)
#




art = crearArticulo("titulo","contenido","autor","fecha","imagen","tags")


insertar(art)


leer()

conexion.commit()
conexion.close()