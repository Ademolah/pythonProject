
class Heap(object):  #this is the implementation of an algorithm that searches or returns objects/values with the highest priority, hence undelying ADS name, priority queue

    HEAP_SIZE = 11

    def __init__(self):
        self.heap = [0] * Heap.HEAP_SIZE
        self.currentPosition = -1   #the last item we inserted

    def insert(self, item):

        if self.isFull():
            print("Heap is full..")
            return

        self.currentPosition = self.currentPosition + 1 #incrementing the tree to be able to insert other figures
        self.heap[self.currentPosition] = item
        self.fixUp(self.currentPosition) #checking to see that we are not violating the priority queue properties

    def fixUp(self, index):  #this also solves for whenever we delete parent node, the root node since it has the highest priority

        parentIndex = int((index  -1 ) //2)   #divide without remainder, the two is because a parent node has two  children

        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]: #if these statements are true then do the following
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            index =parentIndex
            parentIndex = int((index -1 ) //2)

    def get_max(self):

        return self.heap[0] #this is for Maximum heap where the root node at index 0 has the highest value


    def heapsort(self):

        for i in range(0 ,self.currentPosition + 1): #traversing backward from -1 since initially, self.currentposition = -1, NB: the +1 in this code means the next 'last position'
            temp = self.heap[0]              #parent or root index, starting from the parent index
            print("%d " % temp)              #be printing the parent index because the have the highest priority
            self.heap[0] = self.heap[self.currentPosition - i]  #last element iterated
            self.heap[self.currentPosition -i] = temp       #that is the new parent again
            self.fixDown(0 ,self.currentPosition - i -1)

    def fixDown(self, index, upto):

        while index <= upto:

            leftChild = 2 * index + 1
            rightChild = 2 * index + 2

            if leftChild < upto:
                childToSwap = None

                if rightChild > upto:
                    childToSwap = leftChild
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild

                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break

                index = childToSwap
            else:
                break

    def isFull(self):
        if self.currentPosition == Heap.HEAP_SIZE:
            return True
        else:
            return False

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[1]


if __name__ == "__main__":
    heap = Heap()
    heap.insert(10)
    heap.insert(-20)
    heap.insert(0)
    heap.insert(2)
    heap.insert(4)
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    heap.insert(20)
    heap.insert(15)
    heap.insert(12)

    heap.heapsort()