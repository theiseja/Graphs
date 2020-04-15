class Graph:
    def __init__(self):
        self.nodes = {}
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def add_edge(self, child, parent):
        self.nodes[child].add[parent]

    def getNeighbors(self, child):
        return self.nodes[child]

class Stack:
    def __init__(self):
        self.storage = []

    def pop(self):
        return self.storage.pop()

    def push(self, item):
        self.storage.append(item)

    def size(self):
        return len(self.storage)

    


def earliest_ancestor(ancestors, starting_node):
    # build graph
    graph = Graph()
    for parent, child in ancestors:
        graph.add_node(child)
        graph.add_node(parent)
        graph.add_edge(child, parent)

        # run dft
        aged_one = dft(graph, starting_node)