import pika
import json

params = pika.URLParameters('amqps://bimotgiv:10GC1c0XEwDhiNrCb7D69J9jq2MYfrf-@prawn.rmq.cloudamqp.com/bimotgiv')

conection = pika.BlockingConnection(params)

channel = conection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)    
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)