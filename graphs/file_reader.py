class FileReader(object):
    def __init__(self, PATH=None):
        self.PATH = PATH

    def read_file(self):
        directional = True
        verticies = []
        edges = []
        f = open(self.PATH, "r")
        for i, line in enumerate(f.read().splitlines()):
            if i == 0:
                if 'G' in line:
                    directional = False
            elif i == 1:
                verticies = line.split(',')
            else:
                tuple_line = self.line_to_tuple(line)
                edges.append(tuple_line)
                if directional is False:
                    edges.append(
                        (tuple_line[1], tuple_line[0], *tuple_line[2:]))
        f.close()
        return verticies, edges

    # def line_to_tuple(self, line):
    #     # O(n) solution
    #     stack = []
    #     start = True
    #     for char in line:
    #         if char == '(' or char == ')':
    #             continue
    #         elif char == ',':
    #             start = True
    #         else:
    #             if start:
    #                 stack.append(char)
    #                 start = False
    #             else:
    #                 stack.append(stack.pop() + char)
    #     return tuple(stack)

    def line_to_tuple(self, line):
        '''Python's built in methods are 150% faster!'''
        return tuple(line[1:-1].split(','))
