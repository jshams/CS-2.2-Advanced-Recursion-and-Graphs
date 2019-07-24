import sys
from graph import ADTGraph

if __name__ == '__main__':
    PATH = sys.argv[1][:-4] + '_c1' + sys.argv[1][-4:]
    g = ADTGraph(PATH)
    print(f'Verticies: {g.vertex_count}')
    print(f'Edges: {g.edge_count}')
    print(f'Edge List: { g.edges }')
