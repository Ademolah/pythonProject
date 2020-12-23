#LIFO (last in first out)

class Stack:

    def __init__(self):
        self.stack = []


     #LIFO, inserting the first item with the push function push()
    def push(self, data):
        self.stack.append(data)

    #Pop(), removing and returning the last item // O(1)
    def pop(self):

        if self.stack_size() < 1:
            return -1 #meaning the stack is empty

        data = self.stack[-1]
        del self.stack[-1]

        return data

    #peek() returning the last item // O(1)
    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


stack = Stack()

stack.push(23)
stack.push(2)
stack.push(76)
stack.push(9)
stack.push(54)

print('Size: %d' % stack.stack_size())
print('Popped item: %d' % stack.pop())
print('Size: %d' % stack.stack_size())
print('Peek: %d ' % stack.peek())
print('Size: %d' % stack.stack_size())
print('Popped item: %d' % stack.pop())
print('Size: %d' % stack.stack_size())
print('Peek: %d ' % stack.peek())
print('Size: %d' % stack.stack_size())
print('Popped item: %d' % stack.pop())
print('Popped item: %d' % stack.pop())
print('Popped item: %d' % stack.pop())
print('Popped item: %d' % stack.pop())

