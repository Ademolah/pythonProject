
class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None

class Linkedlist:

    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    #inserting the nodes at the beginning at O(1) time complexity
    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        if not self.head: #if self.head is None
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    #inserting the node at the end takes O(N) time complexity bcos we have to iterate  through the linked list
    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        actual_node = self.head
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def remove(self, data):
        if self.head is None:
            return

        self.numOfNodes = self.numOfNodes - 1

        actual_node = self.head #actual node is the node we want to remove
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode

         #This is called search miss, the item is not present in the linkedlist
        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.nextNode

        else:
            previous_node.nextNode = actual_node.nextNode #updating the refrences

    def size_of_list(self):
        return self.numOfNodes

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)

            actual_node = actual_node.nextNode #updating the references

linked_list = Linkedlist()


linked_list.insert_start(10)
linked_list.insert_start('Charles')
linked_list.insert_start(6)
linked_list.insert_start(7)
linked_list.insert_end(2)

linked_list.remove(34)




linked_list.traverse()



