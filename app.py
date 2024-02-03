# app.py
from flask import Flask, jsonify
from bayeta import frotar
app = Flask(__name__)

@app.route('/')
def index():
    # Llama a la función frotar sin limitar la cantidad de frases
    resultado_frotar = frotar()

    # Devuelve una frase auspiciosa aleatoria en la respuesta de la ruta raíz
    return resultado_frotar[0]['frase']

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def obtener_frases(n_frases):
    resultado_frotar = frotar(n_frases)
    return jsonify({"frases": resultado_frotar})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
