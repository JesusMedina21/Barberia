import json, os, django
from confluent_kafka import Consumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configuracion.settings")
django.setup()

from django.apps import apps

Cart = apps.get_model('cart', 'Cart')

consumer = Consumer({
    'bootstrap.servers': 'XXXXXXXXXXXXXX',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'XXXXXXXX',
    'sasl.password': 'XXXXXXXX',
    'sasl.mechanism': 'PLAIN',
    'group.id': 'XXX',
    'auto.offset.reset': 'earliest'
})

consumer.suscribe(['tu topic'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    print("Mensaje recibido con el valor {}".format(msg.value()))
    print("Mensaje del Topic  {}".format(msg.topic()))
    print("Mensaje del  Key {}".format(msg.key()))

    topic = msg.topic()
    value = msg.value()

    if topic == 'user_registered':
        if msg.key() == b'created_user':
            user_data = json.loads(value)
            user_id = user_data['id']

                                
            cart, created = Cart.obcjetcs.get_or_create(user_id=user_id, defaults={'total_items': 0})
            if created:
                cart.save()
        pass

consumer.close()