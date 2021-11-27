from syncronised_queue import Message, PubSubService, MyPublisher, MyConsumer

if __name__ == '__main__':
    pub_sub_service = PubSubService()
    publisher = MyPublisher()

    message = Message("Nikhil", "marks")
    publisher.publish(message, pub_sub_service)
    message = Message("Vijay", "marks")
    publisher.publish(message, pub_sub_service)
    message = Message("Tipu Sultan", "marks")
    publisher.publish(message, pub_sub_service)

    consumer_a = MyConsumer()
    consumer_a.add_consumer("marks", pub_sub_service)
    consumer_a.poll()

    pub_sub_service.broadcast()
