# Pequeño tutorial sobre Bases de Datos en SQLite3

SQLite es una base de datos relacional de código abierto que se utiliza ampliamente en aplicaciones móviles y de escritorio. Es una buena opción para aplicaciones que no requieren una base de datos de gran tamaño o que necesitan acceder a los datos de forma rápida y sencilla. 

## Diferencias principales entre mySQL y SQLite

| Característica | SQLite | MySQL | 
|---|---|---| 
| Motor de base de datos | In-memory | Almacenamiento en disco | 
| Tamaño de la base de datos | Pequeño | Grande | 
| Velocidad | Rápido | Lento | 
| Facilidad de uso | Fácil | Difícil | 
| Soporte de SQL | Sí | Sí | 
| Licencia | GPL | Propietaria | 
| Duck Typing | **SI** | No | 
|  |  |  | 
|  |  |  | 
La principal ventaja de SQLite es que funciona con la filosofía de Duck Typing, que es una práctica de programación orientada a objetos que permite que las clases de una manera más fácil sea reutilizada en otras clases.

## Codigo

Vamos a crear la siguiente tabla
| idUsuario | nombre | email | 
|---|---|---| 
| 1 | Pepe | Pepe@mail.com | 
| 2 | José | Jose@mail.com | 

Luego de la breve introducción, acerco el código que estuve haciendo, para más facil comprensión, el misom no está orientado a objetos, sino que son simplemente las operaciones necesarias para llevar a buen término la creación de una base de datos en SQLIite, esto difiere bastante de si se realizaran en mySQL u otros similares.


### Importar la librería

Muchas funciones de Python vienen en librerías asociadas, por lo que se vuelve necesario importarlas a nuestro código cuando
```
import SQLite3
```

### Crear la conección y el cursor para la misma

Primero hay que crear la conección a la Base de datos y luego crear el cursor que se encarga de las tareas
```
conexion = sqlite3.connect("RUTA y NOMBRE del ARCHIVO.sqlite")
cursor = conexion.cursor()
```

Puede llamarse como se quiera, hasta nombre propio jaja, también puede hacerse con extensión **.db** pero prefiero no hacerlo así para no confundir con el formato apto para mySQL y otros.
con **cursor** se ejecutaran todas las tareas dentro de la base de datos.

### Ejecutar la creación de la tabla

A la hora de ejecutar una tarea, debemos introducir un texto, se hace de la misma manera que en mySQL pero, aprovechando el modelo Duck Typing, no necesitamos especificar el tipo de dato de cada columna, eso sí, **va ha habe que introducir mecanismos de verificación de datos ANTES de guardar los mismos** ésto último no lo cubriré en este archvivo.
```
text = """CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre,
        mail
        );
        """

cursor.execute(text)
```
aquí se crea una tabla llamada **usuarios** con tres columnas, **id** que es único para cada usuario, y los demás datos (es posible agregar cuantos datos se requieran.)

### COMITEAR

La parte más importante del proceso, si no se hace, la base de datos no se crea, y no se guarda cambio alguno.
```
conexion.commit()
```

### Creando usuarios e insertando los mismos

A continuación se muestran las funciones para crear usuarios e insertar los mismos en la Base de Datos.
```
def crearUsuario(nombre, mail):
    usuario={}
    usuario["nombre"]=titulo
    usuario["mail"]=contenido
    return usuario

def insertar(usuario):
    global cursor
    text = """INSERT INTO usuarios (nombre,mail) VALUES  (?,?);"""
    data = (usuario["nombre"], usuario["mail"])
    cursor.execute(text, data)
```
Esto se hace así pues de esta forma (utilizando los signos **?**) se previenen ataques por inyección de datos.


### Introduciendo los datos de los usuarios

Con las siguiente líneas se insertar los dos usuarios mencionados.
```
usuario = crearUsuario("Pepe","Pepe@mail.com")
insertar(usuario)
usuario = crearUsuario("José","Jose@mail.com")
insertar(usuario)
```

### Leyendo los datos de los usuarios

```
def leer():
    global cursor
    cursor.execute("""SELECT * FROM usuarios""")
    elementos = cursor.fetchall()
    for usuario in elementos:
        print(usuario)
```

### Haciendo commit y cerrando conección

Recordar que este paso es importante para que la base de datos guarde todos los elementos, y para evitar que quede expuesta a entradas de datos no deseadas.
```
conexion.commit()
conexion.close()
```
