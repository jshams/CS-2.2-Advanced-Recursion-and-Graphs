'''
Using your Graph ADT code, or in a completely separate program (without a graph class). 
Determine if a given undirected graph is Eulerian (has an Eulerian Cycle). 
Your code should be well documented, tested and organized.

Input: A file containing a undirected graph.

python3 challenge_5.py graph_data.txt

G
1,2,3,4,5
(1,2)
(2,3)
(3,4)
(4,5)
(1,5)
'''


def has_eulerian_cycle(edge_list):
    '''given a list of edges as tuples
        determine whether a eulerian circuit exists
        time complexity: O(n) where n is the number of edges'''
    # create a dictionary with vertices and their degrees
    vertex_degrees = {}
    for vertex_pair in edge_list:
        for vertex in vertex_pair:
            # if the vertex is in our histogram
            if vertex in vertex_degrees:
                # increment its value by one
                vertex_degrees[vertex] += 1
            # if the vertex is not in our histogram
            else:
                # set its value to 1
                vertex_degrees[vertex] = 1
    # iterrate through degrees of vertices
    for val in vertex_degrees.values():
        # if any vertex degree is not divisible by 2
        if val % 2 != 0:
            # return False
            return False
    # if all vertex degrees are divisibly by 2
    return True


def read(path):
    # create an empty array of edges
    edges = []
    # open the file
    f = open(path, "r")
    # read every line in the file
    for i, line in enumerate(f.read().splitlines()):
        # skip the first 2 lines because we are not using a graph class
        if i > 1:
            # turn the line into a tuple
            edge = tuple(line[1:-1].split(','))
            # add the edge to our edge list
            edges.append(edge)
    # close our file
    f.close()
    # return the list of edges
    return edges


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 0:
        path = sys.argv[1]
        edges = read(path)
        has_eul_cyc = has_eulerian_cycle(edges)
        print(f'This graph is Eulerian: {"TRUE" if has_eul_cyc else "FALSE"}')
    else:
        edges = read('graph_data.txt')
        print(has_eulerian_cycle(edges))
