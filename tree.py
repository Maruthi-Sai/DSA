class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def get_level(self, node):
        level = 0
        while node.parent:
            level += 1
            node = node.parent
        return level

    def print(self):
        level = self.get_level(self)
        indent = '   ' * level
        prefix = f'{indent}|__' if level else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print()


mytree = TreeNode('Electronics')
# Laptops
laptops = TreeNode('laptops')
l1 = TreeNode('Lenovo')
l2 = TreeNode('Acer')
l3 = TreeNode('Dell')

laptops.add_child(l1)
laptops.add_child(l2)
laptops.add_child(l3)
mytree.add_child(laptops)

# TV's
tv = TreeNode('Tv\'s')
t1 = TreeNode('Samsung')
t2 = TreeNode('LG')
t3 = TreeNode('Onida')

tv.add_child(t1)
tv.add_child(t2)
tv.add_child(t3)
mytree.add_child(tv)

# SmartPhones
smartphones = TreeNode('smartphones')
p1 = TreeNode('Apple')
p2 = TreeNode('Motorala')
p3 = TreeNode('BlackBerry')

smartphones.add_child(p1)
smartphones.add_child(p2)
smartphones.add_child(p3)
mytree.add_child(smartphones)

mytree.print()