import pika
import os
import json
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RabbitMQProducer:
    def __init__(self):
        # Configuración de conexión desde variables de entorno
        self.cloudamqp_url = os.environ.get('CLOUDAMQP_URL', 'amqps://tqjuxcfa:F5RHgr7e_GNGwD4RetZPH1Bjk6fQtdEb@kebnekaise.lmq.cloudamqp.com/tqjuxcfa')
        self.queue_name = 'user_registered'
        
        # Establecer conexión
        self.params = pika.URLParameters(self.cloudamqp_url)
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()
        
        # Declarar la cola (si no existe se crea)
        self.channel.queue_declare(queue=self.queue_name, durable=True)
    
    def send_message(self, message):
        try:
            self.channel.basic_publish(
                exchange='',
                routing_key=self.queue_name,
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=2,  # hace el mensaje persistente
                ))
            logger.info(f"Message sent to {self.queue_name}: {message}")
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            raise
    
    def close_connection(self):
        self.connection.close()

# Instancia global del producer
producer = RabbitMQProducer()

def send_user_registered_event(user):
    """Envía un evento cuando se registra un nuevo usuario"""
    try:
        # Prepara los datos del usuario
        user_data = {
            'id': str(user.id),
            'email': user.email,
            'username': user.username
        }
        
        # Envía el mensaje a RabbitMQ
        producer.send_message(user_data)
        
    except Exception as e:
        logger.error(f'Error sending user registration event: {e}')