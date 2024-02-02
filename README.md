# La Bayeta de la Fortuna

La Bayeta de la Fortuna es una aplicación web sencilla que proporciona frases auspiciosas aleatorias cada vez que se accede a la web.


# Características

    Implementación de una interfaz web sencilla.
    Acceso a la fortuna al visitar la ruta raíz (/).
    Obtención de frases auspiciosas en formato JSON mediante la ruta /frotar/<n_frases>.


## Instrucciones para ejecutar la aplicación con Docker

Sigue estos pasos para ejecutar la aplicación en un contenedor Docker:

### 1. Clonar el repositorio

    git clone https://github.com/jvm-pps/pps_python_git_docker.git
    cd pps_python_git_docker

### 2. Añadir una nueva red de docker

    docker network create bayeta-network

### 3. Añadir un contenedor de mongodb

    docker run --name mongodb-container --network bayeta-network -p 27017:27017 -d mongo

### 4. Construir la imagen de docker y lanzarla

    docker build -t labayetadelafortuna .
    docker run --name bayeta --network bayeta-network -p 5000:5000 -d labayetadelafortuna

La aplicación estará disponible en http://localhost:5000/

## Cambios Recientes
Versión 1.0.1

    Se ha añadido la funcionalidad de almacenar las frases auspiciosas en una base de datos MongoDB.


## Licencia

Este proyecto está bajo la Licencia GPL-3.0 license - ver el archivo LICENSE para más detalles.


