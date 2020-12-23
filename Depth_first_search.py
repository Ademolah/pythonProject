class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacentList = []
        self.visited = False
        self.predecessor = None



class DepthFirstSearch(object):

    def dfs(self, startNode): #using recursion, we want the operating sysytem stack to be used


        startNode.visited = True
        print(startNode.name)

        for n in startNode.adjacentList:
            if not n.visited:
                self.dfs(n) #calling the n recursively



node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacentList.append(node2)
node1.adjacentList.append(node3)
node2.adjacentList.append(node4)
node4.adjacentList.append(node5)

df = DepthFirstSearch()
df.dfs(node2)
