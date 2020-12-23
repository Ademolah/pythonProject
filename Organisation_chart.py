class Chart:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent

        while p:

            level +=1
            p = p.parent

        return level

    def print_tree(self, property_name):
        if property_name == 'both':
            value = self.name + "( "+ self.designation + ")"

        elif property_name == 'name':
            value = self.name

        else:
            value = self.designation

        spaces = ' ' * self.get_level() * 4

        prefix =  spaces + '|__'  if self.parent else ''

        print(prefix + value)

        if self.children:
            for child in self.children:
                child.print_tree(property_name)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_organisation():

    #CTO hierachy

    Top_head = Chart("VIshwa", "Infrastructure head")
    Top_head.add_child(Chart("Dhaval", "cloud manager"))
    Top_head.add_child(Chart("Abhijit", "Application Manager"))

    CTO = Chart("Chinmay","CTO")
    CTO.add_child(Top_head)
    CTO.add_child(Chart("Aamir","Application Head"))

    #HR hierachy
    HR_HEAD = Chart("Gels","HR head")

    HR_HEAD.add_child(Chart("Peter", "Recruitment"))
    HR_HEAD.add_child(Chart("Waqas", "Policy"))

    root = Chart("Nilupul", "CEO")
    root.add_child(CTO)
    root.add_child(HR_HEAD)



    return root

if __name__ == '__main__':
    root_node = build_organisation()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    #root_node.print_tree('both')



