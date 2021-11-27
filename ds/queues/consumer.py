import syncronised_queue

if __name__ == '__main__':
    consumer_a = syncronised_queue.MyConsumer()
    consumer_a.poll()
