class Addnode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None]*self.v
    
    def add_edge(self, src, dest):
        node = Addnode(src)
        node.next = self.graph[dest]


