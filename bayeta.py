# bayeta.py
from funcion_mongo import instanciacion,consulta

def frotar(n_frases: int = 1) -> list:
    cliente, frases_auspiciosas = instanciacion()
    resultado = consulta(cliente, frases_auspiciosas, n_frases)
    return resultado