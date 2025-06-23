import pika, json

params = pika.URLParameters('amqps://tqjuxcfa:F5RHgr7e_GNGwD4RetZPH1Bjk6fQtdEb@kebnekaise.lmq.cloudamqp.com/tqjuxcfa')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dupms(body), properties=properties)