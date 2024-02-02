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

### 2. Construir la imagen de docker y lanzarla

docker build -t labayetadelafortuna .
docker run -p 5000:5000 labayetadelafortuna

La aplicación estará disponible en http://localhost:5000/.


## Cambios Recientes
Versión 1.0.0

    Se agregó la funcionalidad de frases auspiciosas utilizando bayeta.py.
    Se ajustó la configuración del servidor para escuchar en todas las interfaces.
    Se mejoró la gestión de dependencias utilizando Docker.




## Licencia

Este proyecto está bajo la Licencia GPL-3.0 license - ver el archivo LICENSE para más detalles.


