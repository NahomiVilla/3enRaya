# 3enRaya
![Image text](https://github.com/NahomiVilla/3enRaya/blob/main/imagen.jpg)
## Tabla de Contenido
- [Descripción 📜](#Descripción-)
- [Requisitos 📋](#Requisitos-)
- [Caracteristicas](#Caracteristicas-)
- [Configuración](#Configuración-)

## Descripción
Este proyecto implementa el clásico juego de Tres en Raya (Tic-Tac-Toe) en Python, con una interfaz gráfica de usuario (GUI) construida con la biblioteca Tkinter. El juego cuenta con una pantalla principal en la que los jugadores pueden realizar sus movimientos haciendo clic en los botones dispuestos en un tablero de 3x3.
## Requisitos 
* Python 3.9
* Biblioteca necesaria: tkinter, Pillow.
* Modulos necesarios: time, theards
### Puede instalar la biblioteca utilizando el siguiente comando en la terminal:
```
pip install tk
```
```
pip install Pillow
```
## Caracteristicas
* Interfaz Gráfica Atractiva: La interfaz gráfica se ha diseñado con una imagen de fondo y botones personalizados para proporcionar una experiencia visual agradable al usuario.

* GIF Animados para Jugadores: Cada jugador tiene su propio GIF animado (una cruz para 'X' y un círculo para 'O') que se muestra al realizar un movimiento en el tablero.

* Detección de Ganador y Empate: El juego verifica automáticamente si hay un ganador después de cada movimiento, ya sea por completar una fila, columna, diagonal o antidiagonal. También detecta cuando hay un empate.

* Reinicio del Juego: El juego puede reiniciarse en cualquier momento presionando la tecla de espacio, lo que restablece el tablero y permite que los jugadores comiencen una nueva partida.

* Pantalla Completa y Salida: La aplicación se ejecuta en el modo de pantalla completa. La tecla Escape se puede usar para salir de la aplicación.
## Funcionalidades
* Personalización de Imágenes: El juego permite personalizar las imágenes de las "X", "O" y la imagen de ganador a través de un menú desplegable.
* Cronómetro con Límite de Tiempo: Se incorpora un cronómetro que limita el tiempo de juego. Al alcanzar el límite, se solicita una contraseña para continuar.
* Generador de Contraseñas Mensuales: Se implementa un generador de contraseñas que crea contraseñas mensuales y las envía por correo electrónico.
* Persistencia de Datos: Se guardan y cargan datos relacionados con la fecha de inicio del juego y el tiempo transcurrido, permitiendo reanudar el juego después de reiniciar la aplicación.

## Configuración

1. Asegúrate de tener instaladas las bibliotecas necesarias, que incluyen Tkinter y Pillow (para trabajar con imágenes).
2. Ejecuta el script 3enRaya.py para iniciar el juego.

## Consideraciones
* Las funcionalidades de correo electrónico necesitan credenciales válidas para funcionar correctamente. Asegúrese de proporcionar credenciales correctas en la instancia de la clase GeneradorContraseñas.
* Se espera que las imágenes y recursos necesarios estén presentes para un funcionamiento adecuado del juego.
