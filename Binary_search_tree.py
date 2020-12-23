class BinarySearchTree:

    def __init__(self, data):

        self.data = data
        self.leftChild = None
        self.rigthChild = None

    def add_child(self, data):

        if data == self.data: #because data can not be duplicated in a binary tree
            return

        if data < self.data:

            if self.leftChild: #assuming the left subtree is not empty
                self.leftChild.add_child(data)
            else:

                self.leftChild = BinarySearchTree(data) #assuming the left subtree is empty

        else:

            if self.rigthChild: #assuming the rigth subtree is not empty
                self.rigthChild.add_child(data)

            else:
                self.rigthChild = BinarySearchTree(data) #assuming the rigth subtree is empty

    def in_order_traversal(self): #printnf the tree in order of increasing elements
        elements = []

        #visiting the left subtree

        if self.leftChild:

            elements += self.leftChild.in_order_traversal()

        #visiting the root node
        elements.append(self.data)

        #visiing the rigth subtree

        if self.rigthChild:
            elements += self.rigthChild.in_order_traversal()

        return elements

    def pre_order_traversal(self):

        element = []

        #visit the root node first

        element.append(self.data)

        #visit the left subtree
        if self.leftChild:
            element += self.leftChild.pre_order_traversal()

        #visiting the rigth subtree
        if self.rigthChild:
            element += self.rigthChild.pre_order_traversal()

        return element

    def post_order_traversal(self):

        element = []

        #visiting the left subtree first recursively
        if self.leftChild:
            element += self.leftChild.post_order_traversal()

        #visiting the rigth subtree recursively

        if self.rigthChild:
            element += self.rigthChild.post_order_traversal()

        #visiting the root node

        element.append(self.data)


        return element


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data: #if our value is smaller than data it migth be in the left
            if self.leftChild:
                return self.leftChild.search(val) #search recursively
            else:
                return False

        if val > self.data: #if our value is greater than data it migth be in the rigth

            if self.rigthChild:
                return self.rigthChild.search(val) #search recursively

            else:
                return False

    def delete_node(self, val):
        if val < self.data:
            if self.leftChild:
                self.leftChild = self.leftChild.delete_node(val) #calling the delete function recursively on the val


        elif val > self.data:
            if self.rigthChild:
                self.rigthChild = self.rigthChild.delete_node(val) #calling the delete function recursively on the val

        else:

            if self.leftChild is None and self.rigthChild is None:
                return None

            elif self.leftChild is None:
                return self.rigthChild

            elif self.rigthChild is None:
                return self.rigthChild

            max_val = self.leftChild.find_max()
            self.data = max_val
            self.leftChild = self.leftChild.delete_node(max_val)#this means the new rigth child node is the minimum of the nodes in the rigth subtree that was deleted

            min_val = self.leftChild.find_max()
            self.data = min_val
            self.leftChild = self.leftChild.delete_node(min_val) #if we are deleting from the left subtree, we replace with the maximum data on the left

        return self

    def find_min(self):
        if self.leftChild is None:
            return self.data

        return self.leftChild.find_min()

    def find_max(self):
        if self.rigthChild is None:
            return self.data

        return self.rigthChild.find_max()

def build_tree(elements):

    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [45,23,4,12,67,5,34,8,95,3,5,12,45]
    numbers_tree = build_tree(numbers)
    countries = ['Nigeria','UK','USA','sweden','Pakistan','turkey','cyprus']
    countries_tree = build_tree(countries)
    #print(numbers_tree.in_order_traversal())
    print(numbers_tree.find_max())
    print(numbers_tree.find_min())
    print('is sweden in this list ?',countries_tree.search('sweden'))
    print('is ghana in this list ?', countries_tree.search('ghana'))
    print(countries_tree.in_order_traversal())
    print(countries_tree.post_order_traversal())
    print(countries_tree.pre_order_traversal())

    numbers_tree.delete_node(23)
    print(numbers_tree.in_order_traversal())

