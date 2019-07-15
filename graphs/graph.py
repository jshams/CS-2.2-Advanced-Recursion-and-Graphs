from linkedlist import LinkedList

class Vertex(object):
    def __init__(self, data):
        self.data = data
        self.pointers = LinkedList()

    def points_to(self, pointer):
        self.pointers.append(pointer)
    
    def is_pointing_to(self, pointer):
        return pointer in self.pointers

class ADTGraph(object):
    def __init__(self, FILE_PATH = ''):
        self.FILE_PATH = FILE_PATH
        self.vertices = [] # this is a list of verticies
    
    def __iter__(self):
        for vertex in self.vertices:
            yield vertex

    def add_vertex(self, vert):
        '''adds an instance of Vertex to the graph.'''
        self.vertices.append(Vertex(vert))

    def add_edge(self, fromVert, toVert, weight = None):
        '''Adds a new, weighted, directed edge to the graph that connects two vertices.'''
        fromVert.points_to(toVert)

    def get_vertex(self, vertKey):
        '''finds the vertex in the graph named vertKey.'''
        for vertex in self.vertices:
            if vertex.data == vertKey:
                return vertex

    def get_vertices(self): 
        '''returns the list of all vertices in the graph.'''
        return [vertex.data for vertex in self]

    def get_neighbors(self, x): 
        '''lists all vertices y such that there is an edge from the vertex x to the vertex y.'''
        return [pointer for pointer in x.pointers]

class FileReader(object):
    def __init__(self, PATH = None):
        self.PATH = PATH
    
    def read_from_g(self):
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

def test_FileReader():
    print(FileReader().split_line('(12,353)'))

if __name__ == '__main__':
    test_FileReader()