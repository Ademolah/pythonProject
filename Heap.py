
#we have to bear in mind that the heap is in form of array

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

        return self.heap[0]


    def heapsort(self):

        for i in range(0 ,self.currentPosition + 1):
            temp = self.heap[0]
            print("%d " % temp)
            self.heap[0] = self.heap[self.currentPosition - i]
            self.heap[self.currentPosition -i] = temp
            self.fixDown(0 ,self.currentPosition - i -1)


        #We store the max (in a max heap) or the min (in a in heap) item in the temp variable. So in every iteration we take the root node which is the min (or max item).
        # And we put in into the last slot of the array -
        # we represent the heap with a one-dimensional array if you may recall.
        # So what does it mean? Of course it means that in every iteration we have to deal with fewer and fewer items because we have already considered some items in previous iterations.
        # This is why we have to decrement current_position-i-

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