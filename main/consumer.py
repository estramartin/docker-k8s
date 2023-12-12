import json
import pika


from main import Product, db, app

params = pika.URLParameters('amqps://bimotgiv:10GC1c0XEwDhiNrCb7D69J9jq2MYfrf-@prawn.rmq.cloudamqp.com/bimotgiv')

conection = pika.BlockingConnection(params)

channel = conection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    with app.app_context():
        print('Received in main')
        data = json.loads(body)
        print(data)

        if properties.content_type == 'product_created':
            product = Product(id=data['id'], title=data['title'], imange=data['image'])
            db.session.add(product)
            db.session.commit()        
            print('Product Created')
        elif properties.content_type == 'product_updated':
            product = Product.query.get(data['id'])
            product.title = data['title']
            product.imange = data['image']
            db.session.commit()
            print('Product Updated')
        elif properties.content_type == 'product_deleted':
            product = Product.query.get(data)
            db.session.delete(product)
            db.session.commit()
            print('Product Deleted')
    

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

