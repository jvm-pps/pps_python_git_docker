from pymongo import MongoClient

datos = [
    {"frase": "El éxito es como un fantasma, muchos hablan de él, pero pocos lo han visto de verdad"},
    {"frase": "La aventura de hoy es la historia de terror del mañana"},
    {"frase": "La felicidad es como un rayo de sol, disfrútala antes de que el cambio climático la arruine"},
    {"frase": "Enfrenta tus miedos, o pídeles alquiler por vivir en tu cabeza"},
    {"frase": "Recuerda, cada pequeño cambio cuenta. Especialmente los errores en tu declaración de la renta"},
    {"frase": "Aprovecha las oportunidades, son como los autobuses, los que no llegan tarde simplemente no pasan"},
    {"frase": "Ser agradecido está bien, pero no paga las facturas"},
    {"frase": "La creatividad es como jugar a la ruleta rusa, nunca sabes cuándo te tocará una 'buena' idea"},
    {"frase": "Ríe y el mundo reirá contigo. Llora, y te darán una cuenta de Twitter"},
    {"frase": "Sigue tu corazón, pero recuerda llevar tu cerebro contigo"}
]

def instanciacion():
    # Conexión con el motor de Mongo
    cliente_mongo = MongoClient('mongodb://mongodb-container:27017')
    
    # Conexión con la BD (la crea si no existe)
    bd = cliente_mongo['bayeta']
    
    # Conexión con la tabla (llamada colección en Mongo)
    frases_auspiciosas = bd['frases_auspiciosas']
    
    return cliente_mongo, frases_auspiciosas

def inicializacion(datos):

    # Comprobamos que no se haya inicializado previamente
    if frases_auspiciosas.count_documents({}) == 0:
        # Inserción de datos
        frases_auspiciosas.insert_many(datos)

def consulta(cliente_mongo, frases_auspiciosas, n_frases: int = 1):
    # Obtener frases aleatorias
    frases_aleatorias = list(frases_auspiciosas.aggregate([{'$sample': {'size': n_frases}}]))
    
    # Cerrar cliente
    cliente_mongo.close()

    return frases_aleatorias


# Uso de las funciones
cliente, frases_auspiciosas = instanciacion()
inicializacion(datos)
consulta(cliente, frases_auspiciosas)

