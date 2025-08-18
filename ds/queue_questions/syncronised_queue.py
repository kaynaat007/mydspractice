"""
support of TTL OF EACH message

"""
import threading, queue
import uuid
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from collections import defaultdict


def log(*args):
    print(args)


def get_random(prefix):
    return prefix + "_" + str(uuid.uuid4())


class Message:

    def __init__(self, data, topic, ttl=0):
        self.data = data
        self.ttl = ttl
        self.topic = topic
        self.to_be_executed_at = (datetime.now() + timedelta(seconds=ttl)).timestamp()
        self.id = get_random("message")

    def get_priority(self):
        return self.to_be_executed_at

    def get_topic(self):
        return self.topic


class Consumer(ABC):

    # loop which runs and checks for new messages.
    @abstractmethod
    def poll(self):
        pass

    # add consumer with pub sub service for a topic
    @abstractmethod
    def add_consumer(self, topic, pub_sub_service):
        pass

    # remove consumer with pub sub service for a topic
    @abstractmethod
    def remove_consumer(self, topic, pub_sub_service):
        pass

    # get ID of a consumer
    @abstractmethod
    def get_id(self):
        pass

    # insert a message into subscriber
    @abstractmethod
    def put(self, message):
        pass


class PubSubService:

    def __init__(self):
        self.q = queue.PriorityQueue()
        self.executor = ThreadPoolExecutor(max_workers=3)
        self.topic_subscriber_map = defaultdict(dict)
        self.subscriber_set = set()

    def add_message(self, message):
        self.q.put([message.get_priority(), message])

    def add_subscriber(self, topic, consumer: Consumer):
        consumer_id = consumer.get_id()
        log("adding consumer ", consumer_id)
        self.topic_subscriber_map[topic][consumer_id]  = consumer
        self.subscriber_set.add(consumer_id)
        log("added consumer")

    def remove_subscriber(self, topic, consumer: Consumer):
        consumer_id = consumer.get_id()
        log("removing consumer id: ", consumer_id)
        if consumer_id in self.subscriber_set:
            self.subscriber_set.remove(consumer_id)
        if topic in self.topic_subscriber_map:
            consumer_map = self.topic_subscriber_map[topic]
            if consumer_id in consumer_map:
                del consumer_map[consumer_id]
                log("successfully removed consumer")

    def broadcast(self):
        """
        spin threads to publish message to channel
        """
        log("running pub sub service")
        while True:
            priority, message = self.q.get(block=True)
            topic = message.get_topic()
            log("broadcasting messages for topic: ", topic)
            consumers_topic_map = self.topic_subscriber_map.get(topic)
            for consumer_id, consumer in consumers_topic_map.items():
                consumer.put(message)


class Publisher(ABC):

    @abstractmethod
    def publish(self, message: Message, pub_sub_service: PubSubService):
        pass


class MyConsumer(Consumer):

    def __init__(self):
        self.q = queue.PriorityQueue()
        self.id = get_random("consumer")

    def get_id(self):
        return self.id

    def run(self):
        while True:
            priority, message = self.q.get(block=True)
            log("received message: ", priority, message)
            self.q.task_done()

    def poll(self):
        log("polling started for consumer ", self.id)
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(self.run)
            future.result()

    def put(self, message: Message):
        self.q.put([message.get_priority(), message])

    def add_consumer(self, topic: str, pub_sub_service: PubSubService):
        pub_sub_service.add_subscriber(topic, self)

    def remove_consumer(self, topic: str, pub_sub_service: PubSubService):
        pub_sub_service.remove_subscriber(topic, self)


class MyPublisher(Publisher):

    def publish(self, message: Message, pub_sub_service: PubSubService):
        pub_sub_service.add_message(message)
        log("message has been added to queue")


# publisher = MyPublisher()
# pub_sub_service = PubSubService()
# pub_sub_service.broadcast()
#
# message = Message("Nikhil", "marks")
# publisher.publish(message, pub_sub_service)
# message = Message("Vijay", "marks")
# publisher.publish(message, pub_sub_service)
# message = Message("Tipu Sultan", "marks")
# publisher.publish(message, pub_sub_service)
#
# consumer_a = Consumer()
# consumer_a.poll()



