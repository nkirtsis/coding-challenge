#!/usr/bin/env python
import pika, sys, os, json

from config import rabbitmq
from process import *

mini_batch = list()    
msg_cnt = 0
process = process()

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq['host']))
    channel = connection.channel()

    channel.queue_declare(queue=rabbitmq['queue'])

    def callback(ch, method, properties, body):
    	print(" [x] Received %r" % body)
    	global mini_batch
    	global msg_cnt   
    	global process     
        msg_cnt += 1
        if body != "finished":
        	mini_batch.append(json.loads(body))
        if msg_cnt == int(rabbitmq['mini_batch_size']) or body == "finished":
        	print("data sent to db")        	
        	data = process.store_data(
				"load.event",
				['id', 'event_type', 'username', 'user_email', 'user_type', 'organization_name', 'plan_name', 'received_at'],
				mini_batch)
        	mini_batch = list()
        	msg_cnt = 0


    channel.basic_consume(queue=rabbitmq['queue'], on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)