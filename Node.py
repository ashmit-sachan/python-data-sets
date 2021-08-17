# Class Node helps create a blueprint for each nodal element of
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
