# app.py
from flask import Flask, jsonify
from bayeta import frotar
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Llama a la función frotar sin limitar la cantidad de frases
    resultado_frotar = frotar()    
    # Elige una frase aleatoria de todas las disponibles
    frase_aleatoria = random.choice(resultado_frotar)

    # Devuelve una frase auspiciosa aleatoria en la respuesta de la ruta raíz
    return frase_aleatoria

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def obtener_frases(n_frases):
    frases = frotar(n_frases)
    return jsonify({"frases": frases})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
