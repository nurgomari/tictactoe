#Tic-Tac-Toe

Implementación del clásico tres en raya con el lenguaje Python y el framework Django


## Pre-requisitos

Se necesitará Python 3, si no está instalado en el sistema se puede descargar en la [Página de Python](https://www.python.org/downloads/).

Para ver si está correctamente instalado:

```
python --version
```

## Instalación de requisitos

Para instalar la versión que se ha utilizado en el desarrollo de esta pequeña aplicación

```
pip install -r requirements.txt
```

## Ejecución

Nos vamos a la carpeta del proyecto, aplicacamos las migraciones y ejecutamos el servidor

```
cd tictactoe
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Una vez hecho esto  para jugar, ya que no se ha desarrollado nada de front-end abrimos una consola y usaremos 2 comandos:

Para crear una partida

```
curl.exe -X POST http://127.0.0.1:8000/api/games/ -H "Content-Type: application/json" -d "{\"player_x\": \"{Nombre del jugador 1}\", \"player_o\": \"{Nombre del jugador 2}\"}"
```

Para realizar un movimiento

```
curl -X PATCH http://127.0.0.1:8000/api/games/{id de la partida}/ -H "Content-Type: application/json" -d "{\"position\": {número de la posición donde poner la pieza}, \"player\": \"{X o O según el jugador que realice el movimiento}\"}"
```
La posición debe ser un número entre 0 y 8 ambos incluidos siendo 0 la posición correspondiente a la esquina superior izquierda y 8 la esquina inferior derecha.


## Ejecución de pruebas

Para ejecutar las pruebas ejecutaremos la siguiente línea

```
python manage.py test
```
