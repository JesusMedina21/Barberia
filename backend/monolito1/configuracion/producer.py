from confluent_kafka import Producer
import os

producer = Producer({
    'bootstrap.servers': 'XXXXXXXXXXXXXX',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'XXXXXXXX',
    'sasl.password': 'XXXXXXXX',
    'sasl.mechanism': 'PLAIN',
})