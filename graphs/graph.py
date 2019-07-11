# !Python
from linkedlist import LinkedList

class Vertex(object):
    def __init__(self, data):
        self.data = data
        self.pointers = LinkedList()

    def points_to(self, pointer):
        self.pointers.append(pointer)

class Graph(object):
    def __init__(self, FILE_PATH = ''):
        pass

    def add_vertex(self, vert):
        '''adds an instance of Vertex to the graph.'''
        pass
    def add_edge(self, fromVert, toVert, weight = None):
        '''If weight is None: Adds a new, directed edge to the graph that connects two vertices.
        Else: Adds a new, weighted, directed edge to the graph that connects two vertices.'''
        pass
    def get_vertex(self, vertKey):
        '''finds the vertex in the graph named vertKey.'''
        pass
    def get_vertices(self): 
        '''returns the list of all vertices in the graph.'''
        pass
    def get_neighbors(self, x): 
        '''lists all vertices y such that there is an edge from the vertex x to the vertex y.'''
        pass
