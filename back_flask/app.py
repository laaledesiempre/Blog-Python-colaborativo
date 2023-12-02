
# importamos las librerias necesarias
# Flask es para crear la aplicacion que crea el servidor
# render_template para que el servidor renderise los archivos html
# request para que el server se comunique con los html

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__) # con esta función creamos las aplicación de Flask


@app.route('/') # con estos decoradores le indicamos la ruta donde se encuentran los templates
# en este caso en la carpeta templates (entiendo que por defecto hay que darle ese nombre)

@app.route('/index') # acá le indicamos el template con el que vamos a trabajar
def index():
	return render_template('index.html') # acá le decimos que renderise el template index. Si vamos a index.html vemos que tiene dos botones

# esta seccion seria sql según nos explicó Sebas. En este primer borrador con los campos previstos en el blog
connect = sqlite3.connect('database.db')
connect.execute(
	'CREATE TABLE IF NOT EXISTS BLOG (id INTEGER NOT NULL PRIMARY KEY, categoria TEXT, \
	titulo TEXT, contenido TEXT, autor TEXT, fecha TEXT, etiquetas TEXT)')


@app.route('/crear', methods=['GET', 'POST']) # uno de los botones de index no lleva a este otro temple que sería crear.html. Por eso acá definimos a donde va si le da al boton crear.
# tambien le decimos que va a trabajar con los metodos GET y POST, que son metodos de HTML
# GET es para traer información desde el server a la web y POST para enviar informacion de la
#web al server
def crear():
	if request.method == 'POST': # si vemos el archivo crear.html vemos que el método definido
		# es POST.
		categoria = request.form['categoria'] #acá creamos la variable categoria y con
		# request.form le asignamos el valor que tiene el campo categoria en el crear.html
		titulo = request.form['titulo'] # idem anterior
		contenido = request.form['contenido']
		autor = request.form['autor']
		fecha = request.form['fecha']
		etiquetas = request.form['etiquetas']

# esta parte es sql, con las varibles anteriores completamos la base de datos
		with sqlite3.connect("database.db") as users:
			cursor = users.cursor()
			cursor.execute("INSERT INTO BLOG \
			(categoria,titulo,contenido, autor,fecha, etiquetas) VALUES (?,?,?,?,?,?)",
						(categoria,titulo,contenido, autor,fecha, etiquetas))
			users.commit()
		return render_template("index.html")
	else:
		return render_template('crear.html')


@app.route('/blog') # si en index.html elegimos ver los blog, nos manda acá
# en esta función primero se conecta con la base de datos
def blog():
	connect = sqlite3.connect('database.db')
	cursor = connect.cursor()
	cursor.execute('SELECT * FROM BLOG')

	data = cursor.fetchall() # crea la variable data donde carga la informacion que esta en base
	return render_template("blog.html", data=data) # luego hace un render de blog.html con
	#con los datos cargados en la variable data

# estas ultimas lineas, junto con la primera (linea 10) son las básicas
# para una aplicacin de flask
if __name__ == '__main__':
	app.run(debug=False)
