# pps_python_git_docker
Este repositorio va a contener una aplicacion web llamada "La Bayeta de la Fortuna", la cual nos dira una frase distinta cada vez que entremos a esta.


# Características

- **Experto Web:**
  - Implementación de una interfaz web sencilla.
  - Acceso a la fortuna al visitar la ruta raíz (`/`).
  - Obtención de frases auspiciosas en formato JSON mediante la ruta `/frotar/<n_frases>`.

- **Experto en Python:**
  - Mejora de la lógica interna de la aplicación.
  - Generación aleatoria de frases auspiciosas a partir de una lista almacenada.



## Dependencias

Antes de ejecutar la aplicación, asegúrate de tener Python y `venv` instalados en tu sistema. Puedes crear un entorno virtual y resolver las dependencias ejecutando el siguiente comando:

python -m venv venv
source venv/bin/activate  # En sistemas basados en Unix
.\venv\Scripts\activate   # En sistemas Windows
pip install -r requirements.txt

## Cómo Ejecutar la Aplicación

Asegúrate de tener el entorno virtual activado y ejecuta la aplicación.

*python app.py*

*Accede a la aplicación en tu navegador: http://localhost:5000/*

Recuerda desactivar el entorno virtual cuando hayas terminado:

*deactivate*


