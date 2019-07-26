import sys
from graph import ADTGraph

if __name__ == '__main__':
    PATH = sys.argv[1][:-4] + '_c2' + sys.argv[1][-4:]
    a = sys.argv[2]
    b = sys.argv[3]
    g = ADTGraph(PATH)
    shortest_path = g.shortest_path(a, b)
    print(f'Vertices in shortest path: {", ".join(shortest_path)}')
    print(f'Number of edges in shortest path: {len(shortest_path) - 1}')
