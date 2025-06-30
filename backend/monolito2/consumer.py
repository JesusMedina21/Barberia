import pika
import os
import json
import logging
import django
import uuid

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configuracion.settings")
django.setup()

from apps.cart.models import Cart

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_cart_for_user(user_data):
    """Crea un carrito para el usuario"""
    try:
        user_id = uuid.UUID(user_data['id'])
        
        cart, created = Cart.objects.get_or_create(
            user_id=user_id,
            defaults={
                # Puedes añadir más campos iniciales aquí
            }
        )
        
        if created:
            logger.info(f"Carrito creado para usuario {user_id}")
        else:
            logger.info(f"Carrito ya existía para usuario {user_id}")
            
        return True
    except Exception as e:
        logger.error(f"Error creando carrito: {e}")
        return False

def main():
    try:
        connection = pika.BlockingConnection(
            pika.URLParameters(os.environ['CLOUDAMQP_URL']))
        channel = connection.channel()
        
        channel.queue_declare(queue='user_registered', durable=True)
        
        def callback(ch, method, properties, body):
            try:
                user_data = json.loads(body)
                logger.info(f"Procesando usuario: {user_data['id']}")
                
                if create_cart_for_user(user_data):
                    ch.basic_ack(delivery_tag=method.delivery_tag)
                else:
                    ch.basic_nack(delivery_tag=method.delivery_tag)
                    
            except json.JSONDecodeError:
                logger.error("Mensaje JSON inválido")
                ch.basic_nack(delivery_tag=method.delivery_tag)
            except Exception as e:
                logger.error(f"Error inesperado: {e}")
                ch.basic_nack(delivery_tag=method.delivery_tag)
        
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(
            queue='user_registered',
            on_message_callback=callback,
            auto_ack=False
        )
        
        logger.info("Esperando mensajes...")
        channel.start_consuming()
        
    except KeyboardInterrupt:
        logger.info("Deteniendo consumer...")
        channel.stop_consuming()
    except Exception as e:
        logger.error(f"Error de conexión: {e}")
    finally:
        if 'connection' in locals() and connection.is_open:
            connection.close()

if __name__ == '__main__':
    main()