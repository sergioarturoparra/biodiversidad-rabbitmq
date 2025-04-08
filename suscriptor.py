import pika
import json
import random

# Simulamos el modelo de clasificación (en producción, IA real)
def clasificar_especie(imagen):
    especies_simuladas = ["Solanum lycopersicum", "Capsicum annuum", "Phaseolus vulgaris"]
    return random.choice(especies_simuladas), round(random.uniform(0.85, 0.99), 2)

# Conexión a RabbitMQ
conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()

# Declarar la cola
canal.queue_declare(queue='clasificacion_especies')

# Función de procesamiento
def procesar_mensaje(ch, method, properties, body):
    datos = json.loads(body)
    especie, certeza = clasificar_especie(datos["imagen"])

    print("📥 Datos recibidos desde agricultor:")
    print(f"🧑 Usuario: {datos['usuario_id']}")
    print(f"📸 Imagen: {datos['imagen']}")
    print(f"📍 Ubicación: {datos['ubicacion']}")
    print(f"🔍 Clasificación: {especie} ({certeza * 100}% certeza)")

# Escuchar mensajes
canal.basic_consume(queue='clasificacion_especies', on_message_callback=procesar_mensaje, auto_ack=True)

print("🤖 Esperando imágenes para clasificar...")
canal.start_consuming()