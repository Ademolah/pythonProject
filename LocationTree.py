
class LocationTree:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None


    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        if self.get_level() > level :
            return

        spaces = ' ' * self.get_level() * 4

        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def get_location():

    Global = LocationTree('Global')

    #sub locations
    Gujarat = LocationTree('Gujarat')
    Gujarat.add_child(LocationTree('Ahmedabad'))
    Gujarat.add_child(LocationTree('Baroda'))

    Karnataka = LocationTree('Karnataka')
    Karnataka.add_child(LocationTree('Bangluru'))
    Karnataka.add_child(LocationTree('Mysore'))

    #India locations
    India = LocationTree('India')
    India.add_child(Gujarat)
    India.add_child(Karnataka)

    #USA locations
    #sublocations 3

    New_Jersey = LocationTree('New_jersey')
    New_Jersey.add_child(LocationTree('Princeton'))
    New_Jersey.add_child(LocationTree('Trenton'))

    California = LocationTree('California')
    California.add_child(LocationTree('San Francisco'))
    California.add_child(LocationTree('Mountain View'))
    California.add_child(LocationTree('Palo Alto'))


    USA = LocationTree('USA')
    USA.add_child(New_Jersey)
    USA.add_child(California)

    #top location

    Global.add_child(India)
    Global.add_child(USA)

    return Global





if __name__ == '__main__':
    root_node = get_location()
    root_node.print_tree(2)
    pass



