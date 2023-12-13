import pika
import json

params = pika.URLParameters('')

conection = pika.BlockingConnection(params)

channel = conection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)    
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)