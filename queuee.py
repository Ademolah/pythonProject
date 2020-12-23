# FIFO : first in first out

class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    # O(1) running time complexity
    def enqueue(self, data):  #means add data to the queue
        self.queue.append(data)

    # O(N) running time complexity
    def dequeue(self):
        if self.size_queue() < 1:
            return -1

        data = self.queue[0]
        del self.queue[0]

        return data

    # O(1) running time complexity
    def peek(self):
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print('Size of queue: %d' % queue.size_queue())
print('Dequeued item: %d' % queue.dequeue())
print('Peek: %d' % queue.peek())

print('Size of queue: %d' % queue.size_queue())
print('Dequeued item: %d' % queue.dequeue())
print('Peek: %d' % queue.peek())

print('Size of queue: %d' % queue.size_queue())
print('Dequeued item: %d' % queue.dequeue())
print('Peek: %d' % queue.peek())


