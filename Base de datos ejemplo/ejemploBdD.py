import sqlite3

# Crear la conección y el cursor para la misma
conexion = sqlite3.connect("Blog-Python-colaborativo/Base de datos ejemplo/mi_base_de_datos.sqlite")
cursor = conexion.cursor()

# Ejecutar la creación de la tabla
text = """CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre,
        mail
        );
        """
cursor.execute(text)

# COMITEAR
conexion.commit()

# Creando usuarios e insertando los mismos
def crearUsuario(nombre, mail):
    usuario={}
    usuario["nombre"]=nombre
    usuario["mail"]=mail
    return usuario
def insertar(usuario):
    global cursor
    text = """INSERT INTO usuarios (nombre,mail) VALUES  (?,?);"""
    data = (usuario["nombre"], usuario["mail"])
    cursor.execute(text, data)

usuario = crearUsuario("Pepe","Pepe@mail.com")
insertar(usuario)
usuario = crearUsuario("José","Jose@mail.com")
insertar(usuario)

# Leyendo los datos de los usuarios
def leer():
    global cursor
    cursor.execute("""SELECT * FROM usuarios""")
    elementos = cursor.fetchall()
    for usuario in elementos:
        print(usuario)

leer()
# Haciendo commit y cerrando conección
conexion.commit()
conexion.close()