# Introducción a bootle
## Creando el entorno virtual de desarrollo
Para empezar a usar bottle creamos un entorno virtual de desarrollo.

En la carpeta raíz de nuestro proyecto ejecutamos:

```bash
$ python3 -m venv .venv
```

Lo activamos ejecutando:

```bash
$ source .venv/bin/activate
```

El prompt del sistema aparecerá como:

```bash
(.venv) $
```

Esto nos va a permitir empaquetar nuestra aplicación con todas sus dependencias en una carpeta.

## Instalación de bottle

Utilizando el gestor de paquetes de Python, instalamos bottle.
```bash
(.venv) $ pip install bottle       
Collecting bottle
  Using cached bottle-0.12.19-py3-none-any.whl (89 kB)
Installing collected packages: bottle
Successfully installed bottle-0.12.19
```

## Comprobación de funcionamiento

creamos en el raíz del proyecto un fichero `hello.py` con el siguiente contenido:

```python
from bottle import route, run

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
```
Para combrobar que la aplicación funciona

Ejecutamos el script

```bash
(.venv) $ python hello.py
Bottle v0.12.19 server starting up (using WSGIRefServer())...
Listening on http://localhost:8080/
Hit Ctrl-C to quit.
```

Y a continuación introducimos en el navegador la URL [http://localhost:8080/hello/world](http://localhost:8080/hello/world).

## Configuración inicial de la aplicación

Empezamos creando la base de datos. Para ello creamos en la subcarpeta `config` un fichero con el nombre `create_database.py` con el siguiente contenido:

```python
import sqlite3
def create_database(db_file):
    conn = sqlite3.connect(db_file) # Warning: This file is created in the current directory
    conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
    conn.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
    conn.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
    conn.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
    conn.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
    conn.commit()
```

Creamos en la carpeta inicial del proyecto un fichero `bootstrap.py` con el siguiente contenido:

```python
from config.create_database import create_database

if __name__ == '__main__':
    db_file = 'todo.db'
    create_database(db_file)
```

Solo se debería ejecutar una vez y es el encargado de crear la base de datos e insertar en la misma los datos iniciales.

lo ejecutamos:

```bash
(.venv) $ python bootstrap.py
```

el fichero `hello.py` ya no lo necesitamos, así que lo podemos eliminar:

```bash
(.venv) $ rm hello.py
```
## Recursos

* [Bottle - Web oficial del proyecto](http://bottlepy.org/)
* [Bottle - Documentación](https://bottlepy.org/docs/dev/index.html)