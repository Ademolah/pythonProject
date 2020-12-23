
#tree is a recursive data structure

class TreeNode:

    def __init__(self, data):

        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self  #the child's parent is self
        self.children.append(child)

    def get_level(self):  #getting the level of the each parent nodes
        level = 0
        p = self.parent
        while p:

            level += 1
            p = p.parent

        return level

    def print_tree(self):

        spaces = ' ' * self.get_level() * 7

        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():

    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('HP'))
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Asus'))

    cellphones = TreeNode('cellphones')
    cellphones.add_child(TreeNode('Redmi'))
    cellphones.add_child(TreeNode('Samsung'))
    cellphones.add_child(TreeNode('iphone'))

    tv = TreeNode('Tv')
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Toshiba'))



    root.add_child(laptop)
    root.add_child(cellphones)
    root.add_child(tv)

    print(cellphones.get_level())
    return root



if __name__ == '__main__':
    root =build_product_tree()
    print(root.get_level())
    root.print_tree()