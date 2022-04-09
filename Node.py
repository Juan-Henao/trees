class Node(object):
    def __init__(self, key: int, capacity=0, parent=None):
        self.key = key
        self.parent = None
        self.children = list()
        self.capacity = capacity
        self.availability = capacity

        self.set_parent(parent)

    def set_parent(self, parent):
        if parent and self.parent is not parent and parent.availability != 0:
            self.parent = parent

    def add_child(self, node):
        if len(self.children) <= self.availability:
            node.set_parent(self)
            self.availability = self.availability - 1
            self.children.append(node)
