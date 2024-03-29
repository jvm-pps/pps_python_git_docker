# Fase de resolución de dependencias
FROM python:3.10-slim AS builder

WORKDIR /app

# Copia solo los archivos necesarios para resolver las dependencias
COPY requirements.txt .

# Instala las dependencias en el entorno virtual
RUN python -m venv venv && \
    venv/bin/pip install --no-cache-dir -r requirements.txt

# Fase de ejecución
FROM python:3.10-slim AS runner

WORKDIR /app

# Copia el entorno virtual y la aplicación desde la fase de resolución de dependencias
COPY --from=builder /app/venv venv
COPY . .

# Copia los archivos necesarios para la aplicación
COPY bayeta.py .
COPY frases.txt .
COPY funcion_mongo.py .

COPY panda.png /app/static/panda.png

# Comando para ejecutar la aplicación
CMD ["venv/bin/python", "app.py"]
