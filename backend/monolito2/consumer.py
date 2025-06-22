import pika 

params = pika.URLParameters('amqps://tqjuxcfa:F5RHgr7e_GNGwD4RetZPH1Bjk6fQtdEb@kebnekaise.lmq.cloudamqp.com/tqjuxcfa')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch,method,properties,body):
    print('Recibido en el admin')
    print(body)

channel.baisc_consume(queue='admin', on_message_callback=callback)

print('Se inicializo el consumo')

channel.start_consuming()

channel.close()