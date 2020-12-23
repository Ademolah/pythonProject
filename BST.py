class Node:

    def __init__(self, data, parent):

        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.parent = parent

class BinarySearch:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)  #creating the root node

        else:
            self.insert_node(data, self.root) #this means if there was already a parent node, then insert new node either to left ot right

    def insert_node(self, data, node):
        if data < node.data:

            #we have to go to the left subtree
            if node.leftchild:
                self.insert_node(data, node.leftchild)

            else:
                node.leftchild = Node(data, node)

        else:

            #we have to go to the right subtree
            if node.rightchild:
                self.insert_node(data, node.rightchild)

            else:
                node.rightchild = Node(data, node)

    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.leftchild)
        elif data > node.data:
            self.remove_node(data, node.rightchild)
        else:

            if node.leftchild is None and node.rightchild is None:
                print("Removing a leaf node...%d" % node.data)

                parent = node.parent

                if parent is not None and parent.leftchild == node:
                    parent.leftchild = None
                if parent is not None and parent.rightchild == node:
                    parent.rightchild = None

                if parent is None:
                    self.root = None

                del node

            elif node.leftchild is None and node.rightchild is not None:  # node !!!
                print("Removing a node with single right child...")

                parent = node.parent

                if parent is not None:
                    if parent.leftchild == node:
                        parent.leftchild = node.rightchild
                    if parent.rightchild == node:
                        parent.rightchild = node.rightchild
                else:
                    self.root = node.rightchild

                node.rightchild.parent = parent
                del node

            elif node.rightchild is None and node.leftchild is not None:
                print("Removing a node with single left child...")

                parent = node.parent

                if parent is not None:
                    if parent.leftchild == node:
                        parent.leftchild = node.leftchild
                    if parent.rightchild == node:
                        parent.rightchild = node.leftchild
                else:
                    self.root = node.leftchild

                node.leftchild.parent = parent
                del node

            else:
                print('Removing node with two children....')

                predecessor = self.get_predecessor(node.leftchild)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.rightchild:
            return self.get_predecessor(node.rightchild)

        return node

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.rightchild:
            return self.get_max(node.rightchild)

        return node.data

    def min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftchild:
            return self.get_min(node.leftchild)

        return node.data



    def traverse_in_order(self, node):

        if node.leftchild:
            self.traverse_in_order(node.leftchild)

        print('%s' % node.data)

        if node.rightchild:
            self.traverse_in_order(node.rightchild)


bst = BinarySearch()

bst.insert(20)
bst.insert(3)
bst.insert(5)
bst.insert(76)
bst.insert(455)

bst.remove(5)

print('Max item is: %d' % bst.get_max(bst.root))
print('Min value is: %d' % bst.get_min(bst.root))

bst.traverse()

