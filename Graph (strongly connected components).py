class Graph:

    def __init__(self, edges): #the route argument will be edges instead of routes
        self.edges = edges #the edges connect the graphs its like towers at the airports
        self.graph_dict = {}

        for start, end in self.edges: #we are going through all the edges here, the tuple
          #Note in above for loop, the key is the starting point
            if start in self.graph_dict: #which means mumbai is always there in dictionary
                self.graph_dict[start].append(end)

            else:
                self.graph_dict[start] = [end] #this is when we assume our first record is blank

        print("Graph dict :", self.graph_dict)

    def get_path(self, start, end, path=[]): #this will return all the paths
        path = path + [start]  #its a recursive function

        if start == end: #this are flights within the same city, mostly exhibited by helicopters
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]: #here for example, if the start is mumbai, node will be two values, paris and dubai
            if node not in path:

                new_paths = self.get_path(node, end, path)#recursively calling the function, e.g, paris is node, new york is end, what is the path between these two destinations ?

                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path = []):

        path = path + [start]

        if start == end: #this are flights within the same city, mostly exhibited by helicopters
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self .graph_dict[start]:
            if node not in path:

                new_shortest_path = self.get_shortest_path(node , end, path)

                if new_shortest_path:
                    if shortest_path is None or len(new_shortest_path) < len(shortest_path):
                        shortest_path = new_shortest_path

        return shortest_path





if __name__ == '__main__':
    routes = [
        ("Mumbai","Paris"), #each tuple indicate one route
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York", "Toronto")

    ]

    route_graph = Graph(routes) #creating object of the class Graph, with route as an argument

    #d = {
        #"Mumbai":["paris","Dubai"],
        #"Paris":["Dubai","New York"]

    #}

    start = "Mumbai"
    end = "New York"
    print(f"path between {start} and {end}:", route_graph.get_shortest_path(start, end)) #string formating in python