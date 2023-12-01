# Documento de diseño

## Idea del proyecto:

```
Este proyecto busca elaborar, por etapas, una aplicacion full stack utilizando unicamente python, esto con la intension de que cada uno de sus participantes pueda dominar las areas de desarrollo full stack que desee
```

## Elementos:

La aplicacion recibira por ahora el nombre de "Blog"

El blog contara con **Articulos** los cuales siguen la siguiente estructura:

```
articulo
    categoria -> _____ | proyecto | recurso 
    titulo -> string
    contenido -> string
    autor -> string
    fecha -> date
    etiquetas -> [string]
```

el **blog** contara con un buscador el cual permitira filtrar por:

- Fecha
- Titulo 
- Categoria

el **blog** tambien contara con una seccion para hablar sobre el proyecto y sus participantes

```
[TODO]
```

Por parte de su backend contara con una API con acceso a:

- Articulos (todos)
- Articulos (filtrados)

### Base de datos
Para todo esto, el blog tendra una base de datos relacional con la siguiente estructura:

# Tabla base para la creación de la Base de datos

Es posible cambiar elementos, esto es solo indicativo.
|                  Elemento                  	|              Descripción              	| Necesidad 	| Tipo de dato 	|
|--------------------------------------------	|---------------------------------------	|-----------	|--------------	|
| Título                                     	| Cabecera de los artículos             	|     Sí    	| String       	|
| Contenido                                  	| Cuerpo de los artículos               	|     Sí    	| String       	|
| Autor                                      	| Creador de los artículos              	|     Sí    	| String       	|
| Categoría                                  	| Para agrupar los artículos            	|     Sí    	| Tupla        	|
| Fecha                                      	| Fecha de publicación                  	|     Sí    	| Date         	|
| ~~Hora~~                                   	| ~~Hora de publicación~~               	|     No    	|              	|
| Imagen                                     	| URL de imágenes                       	|     Sí    	| String       	|
| ~~Fecha y hora de lanzamiento automático~~ 	| ~~Sistema de lanzamiento automático~~ 	|     No    	|              	|
| Tags/etiquetas                             	| Sistema de etiquetas temáticas        	|     Sí    	| Tupla        	|


Algunos elementos se han eliminado teniendo en cuenta las sugerencias de los integrantes del equipo de desarrollo.

```
[TODO]
```


## Colores y diseño

```
[TODO]

```
Zzebastian
Vanesa
Diego A Pizza
Swsanita
MartinBabboni
Lauradelapuente
titoferrari
fedefer85
