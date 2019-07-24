from vertex import Vertex
from file_reader import FileReader
from queue import Queue


class ADTGraph(object):
    def __init__(self, FILE_PATH=None):
        self.f = FileReader(FILE_PATH)
        self.vertices = {}  # dictionary of verticies
        self.edges = []
        self.vertex_count = 0
        self.edge_count = 0
        if FILE_PATH is not None:
            all_verticies, self.edges = self.f.read_file()
            self.add_verticies(all_verticies)
            self.add_egdes(self.edges)

    def __iter__(self):
        '''yields each vertex key'''
        for vertex in self.vertices:
            yield vertex

    def add_vertex(self, vert):
        '''adds an instance of Vertex to the graph.'''
        self.vertices[vert] = Vertex(vert)
        self.vertex_count += 1

    def add_verticies(self, verts):
        for vert in verts:
            self.add_vertex(vert)

    def add_edge(self, from_key, to_key, weight=1):
        '''Adds a new, weighted, directed edge to the graph that connects two vertices.'''
        # from_vert = self.get_vertex(from_vert_key)
        # to_vert = self.get_vertex(to_vert_key)
        # if from_vert is None:
        #     raise KeyError(f'{from_vert} key not found in graph')
        # elif to_vert is None:
        #     raise KeyError(f'{to_vert} key not found in graph')
        if from_key not in self.vertices:
            raise KeyError(f'{from_key} vertex not found in graph')
        if to_key not in self.vertices:
            raise KeyError(f'{to_key} vertex not found in graph')
        self.vertices[from_key].points_to(to_key)
        self.edge_count += 1

    def add_egdes(self, edges):
        for edge in edges:
            self.add_edge(*edge)

    def get_vertex(self, vert_key):
        '''finds the vertex in the graph named vertKey. Or returns None if not found'''
        if vert_key in self.vertices:
            return self.vertices[vert_key]

    def get_vertices(self):
        '''returns the list of all vertices in the graph.'''
        return [vertex for vertex in self]

    def get_neighbors(self, x):
        '''lists all vertices y such that there is an edge from the vertex x to the vertex y.'''
        return [pointer for pointer in x.pointers]

    def breadth_first_search(self, start, end):
        seen = {start}
        queue = Queue([start])
        while queue.is_empty() is False:
            vertex = queue.dequeue()
            for pointer in self.vertices[vertex].pointers:
                print(pointer)


if __name__ == '__main__':
    g = ADTGraph('file_reader_test.txt')
    g.breadth_first_search('1', '2')
