import sqlite3

class CursorBdD:
  def __init__(self):
    # Primero hay que crear la conección a la Base de datos
    self.conexion = sqlite3.connect("Blog-Python-colaborativo/Zzebas/basedatos.sqlite")

    # Crear el cursor que se encarga de las tareas
    self.cursor = self.conexion.cursor()

  def imprimir(self):
    print("#"*30)
    print(self.text)
    print("#"*30)

  def comitear(self):
    self.conexion.commit()
    print("Comiteado")

  def desconectar(self):
    self.conexion.close()
    print("Desconectado")

class Datos:
  def __init__(self, titulo, contenido, autor, fecha, imagen, tags):
    self.titulo = titulo
    self.contenido = contenido
    self.autor = autor
    self.fecha = fecha
    self.imagen = imagen
    self.tags = tags

  def insertar(self):
    self.cursor.execute("""INSERT INTO posteos (titulo, contenido, autor, fecha, imagen, tags)
                      VALUES (?, ?, ?, ?, ?, ?);""",
                    (self.titulo, self.contenido, self.autor, self.fecha, self.imagen, self.tags))

  def leer(self):
    self.cursor.execute("""SELECT * FROM posteos;""")
    posts = self.cursor.fetchall()
    return posts



con = CursorBdD()

dato = Datos("titulo", "contenido", "autor", "fecha", "imagen", "tags")

dato.insertar()
con.comitear()

posts = dato.leer()
print(posts)

con.desconectar()
