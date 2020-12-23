class Node(object):

    def __init__(self, character):
        self.character = character
        self.leftNode = None
        self.middleNode = None
        self.rigthNode = None
        self.value = 0

class TST(object):

    def __init__(self):
        self.rootNode = None

    def put(self, key, value):
        self.rootNode = self.putItem(self.rootNode, key, value,0)  #keep putting value in the first index

    def putItem(self, node, key, value, index):

        c = key[index]

        if node == None:  #if no initial node
            node = Node(c)  #then we instantiate the node with the given character

        if c < node.character:
            node.leftNode = self.putItem(node.leftNode, key, value, index)  #calling the function recursively

        elif c > node.character:
            node.rigthNode = self.putItem(node.rigthNode, key, value, index) #calling the function recursively

        elif index < len(key)-1:
            node.middleNode = self.putItem(node.middleNode, key, value, index+1) #we keep going down the list at this point, hence the increment

        else:
            node.value = node

        return node

    def get(self, key):

        node = self.getItem(self.rootNode, key, 0)

        if node == None:
            return -1

        return node.value

    def getItem(self,node,  key, index):

        if node == None:
            return None

        c = key[index]

        if c < node.character:
            return self.getItem(node.leftNode, key, index)

        elif c > node.character:
            return self.getItem(node.rigthNode, key, index)

        elif index < len(key) - 1:
            return self.getItem(node.middleNode, key, index +1)

        else:
            return node

if __name__ == '__main__':

    ts = TST()

    ts.put('demola','software engineer')
    ts.put('Charles', 'Excellent')

    print(ts.get('Charles'))