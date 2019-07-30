import sys
from graph import ADTGraph

if __name__ == '__main__':
    PATH = sys.argv[1][:-4] + '_c3' + sys.argv[1][-4:]
    a = sys.argv[2]
    b = sys.argv[3]
    g = ADTGraph(PATH)
    has_path = g.recursive_dfs(a, b)
    # shortest_weighted_path = g.dijkstras(a, b)
    print(
        f'There exists a path between vertex {a} and {b}: {"TRUE" if has_path else "FALSE"}')
    # print(
    #     f'The weight of the minimum weight path between vertex {a} and {b} is: {shortest_weighted_path}')
