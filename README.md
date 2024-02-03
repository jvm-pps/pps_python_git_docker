# La Bayeta de la Fortuna

La Bayeta de la Fortuna es una aplicación web sencilla que proporciona frases auspiciosas aleatorias cada vez que se accede a la web.


# Características

    Implementación de una interfaz web sencilla.
    Acceso a la fortuna al visitar la ruta raíz (/).
    Obtención de frases auspiciosas en formato JSON mediante la ruta /frotar/<n_frases>.
    Almacenamiento de las frases auspiciosas en una base de datos MongoDB.
    Despliegue de la aplicación en un contenedor Docker con docker-compose.


## Instrucciones para ejecutar la aplicación con Docker

Sigue estos pasos para ejecutar la aplicación en un contenedor Docker:

### 1. Clonar el repositorio

    git clone https://github.com/jvm-pps/pps_python_git_docker.git
    cd pps_python_git_docker

### 2. Lanzar el contenedor

    docker-compose up -d

    ** Si la imagen no está disponible, se construirá automáticamente.**

La aplicación estará disponible en http://localhost:5000/

### 3. Detener el contenedor

    docker-compose down

## Uso de la aplicación

La aplicación proporciona dos rutas:

    - /: Muestra una frase auspiciosa aleatoria.
    - /frotar/<n_frases>: Devuelve n_frases frases auspiciosas en formato JSON.

## Requisitos

    Sera necesario tener instalado docker y docker-compose en el sistema.
    Si no los tienes instalados, puedes seguir las instrucciones en la documentación oficial de Docker:
    
https://docs.docker.com/get-docker/

## Cambios Recientes
Versión 1.0.2

    - Se ha añadido un archivo docker-compose.yml para el despliegue de la aplicación en un contenedor Docker.
    - Se ha solucionado un error en funcion_mongo.py para que funcione correctamente con la funcion frotar.
    - 

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:

    1. Haz un fork del proyecto.
    2. Crea una rama con tu funcionalidad: `git checkout -b mi-funcionalidad`
    3. Realiza un commit con tus cambios: `git commit -m 'Añadir mi funcionalidad'`
    4. Sube tu rama: `git push origin mi-funcionalidad`
    5. Abre un pull request.

## Autores

-   **Javier Valle** - [jvm-pps]


## Licencia

Este proyecto está bajo la Licencia GPL-3.0 license - ver el archivo LICENSE para más detalles.


