import sqlite3


class CursorBdD():
    def __init__(self):
        # Primero hay que crear la conección a la Base de datos
        self.conexion = sqlite3.connect("Blog-Python-colaborativo/Zebas.sqlite")

        # Crear el cursor que se encarga de las tareas
        self.cursor = self.conexion.cursor()
        # Puede llamarse como se quiera, hasta nombre propio jaja

        self.text = """CREATE TABLE IF NOT EXISTS posteos (
                idPost INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo,
                contenido,
                autor,
                fecha,
                imagen,
                tags
                );
                """
    
        self.cursor.execute(self.text)
        self.conexion.commit()

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
#
class Articulo():
    def __init__(self,titulo,contenido,autor,fecha,imagen,tags):
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.fecha = fecha
        self.imagen = imagen
        self.tags = tags
    
    def imprimirA(self):
        print(self.titulo)
        print(self.contenido)
        print(self.autor)
        print(self.fecha)
        print(self.imagen)
        print(self.tags)
#

class Datos(CursorBdD):

    def crearArticulo(self,titulo,contenido,autor,fecha,imagen,tags):
        return Articulo(titulo,contenido,autor,fecha,imagen,tags)
    
    def insertar(self,articulo):
        text = """INSERT INTO posteos (titulo,contenido,autor,fecha,imagen,tags) VALUES  (?,?,?,?,?,?);"""
        data = (articulo.titulo, articulo.contenido,articulo.autor,articulo.fecha,articulo.imagen,articulo.tags)

        self.cursor.execute(text, data)

    # Esta función es únicamente informativa, TOTALMENTE innecesaria, sólo la utilizo para visualisar la consulta realizada
    def imprimir(self,articulo):
        text = """INSERT INTO posteos (titulo,contenido,autor,fecha,imagen,tags) VALUES  (?,?,?,?,?,?);"""
        data = (articulo.titulo, articulo.contenido,articulo.autor,articulo.fecha,articulo.imagen,articulo.tags)
        print(text, data)
        
    def leer(self):
        self.cursor.execute("""SELECT * FROM posteos""")
        elementos = self.cursor.fetchall()
        for post in elementos:
            print(post)
#



con = CursorBdD()
datos = Datos()
art = datos.crearArticulo("titulo","contenido","autor","fecha","imagen","tags")


datos.insertar(art)
datos.comitear()
datos.imprimir(art)

datos.leer()
con.desconectar()