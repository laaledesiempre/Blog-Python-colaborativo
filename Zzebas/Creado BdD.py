import sqlite3


class CursorBdD:
    def __init__(self):
        # Primero hay que crear la conección a la Base de datos
        self.conexion = sqlite3.connect("Blog-Python-colaborativo/Zzebas/basedatos.sqlite")

        # Crear el cursor que se encarga de las tareas
        self.cursor = self.conexion.cursor()
        # Puede llamarse como se quiera, hasta nombre propio jaja

        self.text = """CREATE TABLE IF NOT EXISTS posteos (
                idPost INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo VARCHAR(45) NOT NULL,
                contenido TEXT NOT NULL,
                autor VARCHAR (30)  NOT NULL,
                fecha DATE NOT NULL,
                imagen VARCHAR (45) NOT NULL,
                tags VARCHAR (45) NOT NULL
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

class Datos(CursorBdD):
    def __init__(self,titulo,contenido,autor,fecha,imagen,tags):
        super().__init__()
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.fecha = fecha
        self.imagen = imagen
        self.tags = tags

    def insertar(self):
        text = """INSERT INTO posteos (titulo,contenido,autor,fecha,imagen,tags) VALUES  (?,?,?,?,?,?);"""
        data = (self.titulo, self.contenido,self.autor,self.fecha,self.imagen,self.tags)

        self.cursor.execute(text, data)
        # self.cursor.execute("""INSERT INTO posteos (titulo,contenido,autor,fecha,imagen,tags) VALUES  (?,?,?,?,?,?);""",("titulo","contenido","autor","fecha","imagen","tags"))

    def leer(self):
        self.cursor.execute("""SELECT * FROM posteos""")
        post = self.cursor.fetchall()
        print(post)




con = CursorBdD()

datos = Datos("titulo","contenido","autor","fecha","imagen","tags")

datos.insertar()
datos.comitear()
datos.imprimir()


con.desconectar()