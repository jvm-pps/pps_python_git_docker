# app.py
from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola, mundo desde Flask!'

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def obtener_frases(n_frases):
    frases = frotar(n_frases)
    return jsonify({"frases": frases})

if __name__ == '__main__':
    app.run(debug=True)
