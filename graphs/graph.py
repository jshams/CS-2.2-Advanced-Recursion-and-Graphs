from linkedlist import LinkedList

class Vertex(object):
    def __init__(self, data):
        self.data = data
        self.pointers = LinkedList()

    def points_to(self, pointer):
        self.pointers.append(pointer)

class ADTGraph(object):
    def __init__(self, FILE_PATH = ''):
        self.FILE_PATH = FILE_PATH
        self.vertices = [] # this is a list of verticies
        self.nodes = [] # nodes are all the verticies' datas

    def read_from_g(self, FILE_PATH):
        pass

    def split_line(self, line):
        v1 = ''
        v2 = ''
        first = True
        for char in line:
            if char == ',':
                first = False
            elif char != '(' and char != ')':
                if first:
                    v1 += char
                else:
                    v2 += char
        if v1.isdigit():
            v1 = int(v1)
        if v2.isdigit():
            v2 = int(v2)
        return v1, v2

    def add_vertex(self, vert):
        '''adds an instance of Vertex to the graph.'''
        self.vertices.append(Vertex(vert))

    def add_edge(self, fromVert, toVert):
        '''Adds a new, directed edge to the graph that connects two vertices.'''
        pass
    def add_edge(self, fromVert, toVert, weight):
        '''Adds a new, weighted, directed edge to the graph that connects two vertices.'''
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


    


def test_ADTGraph():
    print(ADTGraph().split_line('(12,353)'))

if __name__ == '__main__':
    test_ADTGraph()