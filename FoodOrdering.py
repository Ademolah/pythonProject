# queue is first in first out FIFO data structure

from collections import deque
import time
import threading


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print('Queue is empty')
            return


        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


food_ordering = Queue()


def food_order(orders):
    for order in orders:
        print('ordering :', order)
        food_ordering.enqueue(order)
        time.sleep(1)


def serve_food():
    time.sleep(1)

    while True:
        order = food_ordering.dequeue()
        print('serving... ', order)
        time.sleep(2)




if __name__ == '__main__':
    t = time.time()

    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger','pizza', 'samosa', 'pasta', 'biryani', 'burger','moi-moi','garri','santana','eba']

    order1 = threading.Thread(target=food_order, args=(orders,))
    orders2 = threading.Thread(target=serve_food)

    order1.start()
    orders2.start()

    order1.join()
    orders2.join()

    print('process completed in :', time.time() - t, 'seconds')
