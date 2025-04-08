# biodiversidad-rabbitmq
Repositorio del modelo publicador-subscriptor
Este proyecto implementa el patrón arquitectónico *Publicador-Suscriptor* utilizando *RabbitMQ* para distribuir información sobre biodiversidad vegetal capturada por sensores y módulos de IA en áreas agrícolas. Forma parte del caso de estudio: Transformando la agricultura con inteligencia artificial.

---

## 📌 Caso de Uso

*Nombre:* Notificación y almacenamiento de nueva especie vegetal identificada  
*Actor Principal:* Sistema de monitoreo IA (sensor o dron con IA)  
*Descripción:* Cuando se detecta una nueva especie, los datos son publicados y distribuidos en tiempo real al chatbot, dashboard y sistema de almacenamiento.

---

## 🧱 Arquitectura del Sistema

El sistema sigue una arquitectura desacoplada basada en RabbitMQ:


> Ver diagrama completo en el informe/documentación UML.

---

## 📂 Estructura del Repositorio

├── publicador.py # Publicador que envía mensajes sobre especies ├── suscriptor_chatbot.py # Cliente suscriptor para chatbot ├── suscriptor_dashboard.py # Cliente suscriptor para panel de control ├── suscriptor_db.py # Cliente suscriptor para base de datos ├── README.md # Este archivo

---

## 🧪 Instrucciones de uso

### Requisitos:
- Python 3
- RabbitMQ (local o Docker)
- Biblioteca pika

### Instalación de dependencias:
```bash
pip install pika
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
