class ADTGraph(object):
    def __init__(self, FILE_PATH = ''):
        self.f = FileReader(FILE_PATH)
        self.vertices = [] # this is a list of verticies
    
    def __iter__(self):
        for vertex in self.vertices:
            yield vertex

    def add_vertex(self, vert):
        '''adds an instance of Vertex to the graph.'''
        self.vertices.append(Vertex(vert))

    def add_edge(self, from_vert, to_vert, weight = 1):
        '''Adds a new, weighted, directed edge to the graph that connects two vertices.'''
        from_vert_vert = self.get_vertex(from_vert)
        to_vert_vert = self.get_vertex(to_vert)
        if from_vert_vert is None:
            raise KeyError('from_vert key not found in graph')
        elif to_vert_vert is None:
            raise KeyError('to_vert key not found in graph')
        else:
            from_vert_vert.points_to(to_vert_vert)

    def get_vertex(self, vertKey):
        '''finds the vertex in the graph named vertKey. Or returns None if not found'''
        for vertex in self.vertices:
            if vertex.data == vertKey:
                return vertex

    def get_vertices(self): 
        '''returns the list of all vertices in the graph.'''
        return [vertex.data for vertex in self]

    def get_neighbors(self, x): 
        '''lists all vertices y such that there is an edge from the vertex x to the vertex y.'''
        return [pointer for pointer in x.pointers]

if __name__ == '__main__':
    pass