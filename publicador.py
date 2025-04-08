import pika
import json

# Simulamos una imagen de planta con metadatos
datos_especie = {
    "usuario_id": "agricultor_123",
    "imagen": "planta_rosa.jpg",  # Aquí podrías usar base64 en una app real
    "ubicacion": "La Esperanza",
    "fecha": "2025-03-29"
}

# Conexión a RabbitMQ
conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()

# Declarar la cola
canal.queue_declare(queue='clasificacion_especies')

# Publicar mensaje en formato JSON
mensaje = json.dumps(datos_especie)
canal.basic_publish(exchange='', routing_key='clasificacion_especies', body=mensaje)

print("📤 Imagen enviada para análisis de especie vegetal")

conexion.close()