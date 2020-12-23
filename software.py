class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next


class linkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):  # this is in constant time complexity O(1)
        node = Node(data, self.head)  # this is a node containing data and the pointer to the next node
        self.head = node  # next node updated

    def print(self):
        if self.head is None:
            print('list is empty')
            return

        itr = self.head
        llstr = ' '

        while itr:
            llstr += str(itr.data) + '-->'  # llstr means linked list string, as we iterate through the nodes, do the following
            itr = itr.next  # itr means iterator through the nodes

        print(llstr)

    def insert_at_end(self, data):  # this is in linear time complexity O(N)
        if self.head is None:  # this is  assuming our linkedlist is blank
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)  # this is when the pointer is pointing to a null hence 'None'

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next

            count += 1

if __name__ == '__main__':


    ll = linkedList()

    ll.insert_at_beginning(20)
    ll.insert_at_beginning(54)
    ll.insert_at_beginning(54)
    ll.insert_at_beginning(76)
    ll.insert_at_end(76)
    ll.insert_values(['demola', 'boma', 'junior', 'debo', 'bella'])
    ll.print()
    ll.remove_at(3)

    ll.print()

