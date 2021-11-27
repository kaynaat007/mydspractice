import threading, queue

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()

# send thirty task requests to the worker
for item in range(30):
    q.put()
print('All task requests sent\n', end='')


# block until all tasks are done
q.join()
print('All work completed')

customers = queue.PriorityQueue() #we initialise the PQ class instead of using a function to operate upon a list.
customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))
while customers:
     print(customers.get())
#Will print names in the order: Riya, Harry, Charles, Stacy.