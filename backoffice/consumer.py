import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backoffice.settings")
django.setup()

from apps.products.models import Product

params = pika.URLParameters('amqps://bimotgiv:10GC1c0XEwDhiNrCb7D69J9jq2MYfrf-@prawn.rmq.cloudamqp.com/bimotgiv')

conection = pika.BlockingConnection(params)

channel = conection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    id = json.loads(body)       
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

