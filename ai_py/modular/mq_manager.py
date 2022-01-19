import pika
from retry import retry
import traceback
from datetime import datetime
RECOVERDELAY = 0.02
JITTER = 0
import logging
LOGGER = logging.getLogger(__name__)

class MQProducer(object):
    def __init__(self, username=None, password=None, host=None, port=None, queue=None, hostname=None, exchange='', routing_key='',
                 *args, **kwargs):
        try:
            self.username = username
            self.password = password
            self.host = host if host else hostname
            self.port = port
            self.queue = queue
            self.exchange = exchange
            if not self.exchange:
                self.exchange = self.queue.replace('queue', 'exchange')
                if 'exchange' not in self.exchange:
                    self.exchange = '{}_exchange'.format(self.exchange)
            self.routing_key = routing_key
        except Exception as e:
            LOGGER.warning('[MQ init error]',)

    def connect_mq(self):
        try:
            if not hasattr(self, 'connection') or self.connection.is_closed:
                credentials = pika.PlainCredentials(self.username, self.password)
                parameters = pika.ConnectionParameters(host=self.host, port=self.port, credentials=credentials,
                                                       # heartbeat=0, retry_delay=0.1,
                                                       socket_timeout=None,
                                                       blocked_connection_timeout=None,
                                                       )
                self.connection = pika.BlockingConnection(parameters)
        except Exception as e:
            LOGGER.error('{}-\n{}. [MQ connect error]'.format(e, traceback.format_exc()))
            raise e

    def channel_mq(self):
        self.connect_mq()
        if not hasattr(self, 'channel') or self.channel.is_closed:
            self.channel = self.connection.channel()

        self.channel.queue_declare(queue=self.queue, durable=True)  # durable 队列持久化
        self.channel.exchange_declare(exchange=self.exchange, durable=True)
        self.channel.queue_bind(exchange=self.exchange, queue=self.queue, routing_key=self.routing_key)

    @retry(pika.exceptions.AMQPConnectionError, delay=RECOVERDELAY, jitter=JITTER)
    def send_data(self, data: str):
        self.channel_mq()
        self.channel.basic_publish(exchange=self.exchange,
                                   routing_key=self.routing_key,
                                   body=data,
                                   properties=pika.BasicProperties(delivery_mode=2))

    def close_connect(self):
        self.connection.close()

    def close_channel(self):
        if not hasattr(self, 'channel'):
            raise ValueError('the object of <MQProducer> has no attr of channel.')
        self.channel.close()

    def __del__(self):
        try:
            if not self.channel.is_closed:
                self.close_channel()
        except Exception as e:
            LOGGER.warning('[MQ channel delete error]')
        try:
            if not self.connection.is_closed:
                self.close_connect()
        except Exception as e:
            LOGGER.error('[MQ connection delete error]')

#
# class MQConsumer(MQProducer):
#     def __init__(self, *args, **kwargs):
#         super(MQConsumer, self).__init__(*args, **kwargs)
#         self.info = kwargs.get('info', None)
#
#     # @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
#     def receive(self, queue=None):
#         if not hasattr(self, 'channel') or self.channel.is_closed:
#             self.channel_mq()
#         if queue is None: queue = self.queue
#         self.channel.basic_consume(on_message_callback=self.callback, queue=queue, auto_ack=False)
#         try:
#             self.channel.start_consuming()
#         # Don't recover connections closed by server
#         except pika.exceptions.ConnectionClosedByBroker as e:
#             pass
#
#     def callback(self, ch, method, properties, body):
#         ch.basic_ack(delivery_tag=method.delivery_tag)
#         print('prop', self.info, properties)
#         print('body', self.info, body)
#         self.mqres.send(body)
#         self.body = body


class MQConsumer(MQProducer):
    def __init__(self, *args, queue=None, **kwargs):
        super(MQConsumer, self).__init__(*args, queue=queue, **kwargs)
        # self.queue = queue
        # self.resultmq = kwargs.get('producer', MQProducer(*args, **kwargs, queue='mq_results_queue'))
        # self._errormq = kwargs.get('error_producer', MQProducer(*args, **kwargs, queue='mq_error_queue'))

    @retry(pika.exceptions.AMQPConnectionError, delay=RECOVERDELAY, jitter=JITTER)
    def receive(self, process_func=None):
        if process_func is None:
            process_func = lambda x: x
        if not hasattr(self, 'channel') or self.channel.is_closed:
            self.channel_mq()

        self.channel.basic_consume(
            on_message_callback=lambda *args, **kwargs: self.callback(*args, func=process_func, **kwargs),
            queue=self.queue, auto_ack=False)
        try:
            self.channel.start_consuming()
        # Don't recover connections closed by server
        except pika.exceptions.ConnectionClosedByBroker as e:
            LOGGER.error('{}-\n{}. [MQ receive error and try to reconnecting.]'.format(e, traceback.format_exc()))


    def callback(self, ch, method, properties, body, func):
        ch.basic_ack(delivery_tag=method.delivery_tag)

        return func(body)
