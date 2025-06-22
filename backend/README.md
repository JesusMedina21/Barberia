# Guía de instalación del proyecto Django

## ¿De que se trata este proyecto?

Este proyecto se esta desarrollando en microservicios en Django para la plataforma Barberia, permitiendo Registrar, Modificar, Eliminar y Listar los Productos. A traves de los metodos GET, POST, PUT y DELETE que proporcionan las diversas APIs de cada servicio.

## Instalaciones necesarias

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop/)

## Antes de comenzar

Antes de comenzar a instalar las dependencias del proyecto es necesario verificar que tienes las dependencias necesarias instaladas.
Abre la terminal de comandos de tu sistema y sigue los siguientes pasos para asegurarte de que todo está correcto antes de comenzar.

### Verificar instalación de Python

```
python --v
```


### Comandos para correr el backend

- Ejecuta el siguiente comando, segun el monolito que deseas correr 

```
cd monolito1 o cd monolito2
```

- Ejecuta el siguiente comando para instalar el proyecto:

## Si estas en Windows

```
docker-compose up 
```


## Si estas en cualquier Distribucion Linux/MacOS 

```
docker compose up
```

Verificas que URL te arrogo la consola. Por ejemplo 127.0.0.1:8000 o localhost:8000 y te dirigas al navegador con la url arrogada.


<h3 align="center">¡Y Listo! Has terminado de correr el backend 🥳</h3>
