class Node(object): #these nodes are also called vertices

    def __init__(self, name):
        self.name = name
        self.adjacentList = []
        self.visited = False
        self.predecessor = None


class BreadthFirstSearch(object):

    #while BFS can be implmented via queue, DFS can be implemented via STACK
    def bfs(self, startNode):

        queue = []
        queue.append(startNode)
        startNode.visited = True   #because we have appended startnode to queue above

        while queue:             #meaning while queue is not empty

            actualNode = queue.pop(0)     #we remove the first index because queue is a FIFO data structure
            print(actualNode.name)

            for n in actualNode.adjacentList:  #we are viviting the neighbors or children of that node
                if not n.visited:     #if that node hasnt been visited
                    n.visited = True  #visit it
                    queue.append(n)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacentList.append(node2)
node1.adjacentList.append(node3)
node2.adjacentList.append(node4)
node4.adjacentList.append(node5)

bf = BreadthFirstSearch()
bf.bfs(node1)
