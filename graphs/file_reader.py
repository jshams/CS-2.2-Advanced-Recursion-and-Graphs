class FileReader(object):
    def __init__(self, PATH=None):
        self.PATH = PATH

    def read_file(self):
        directional = True
        verticies = []
        edges = []
        f = open(self.PATH, "r")
        for i, line in enumerate(f.readlines()):
            if i == 0:
                if 'G' in line:
                    directional = False
            elif i == 1:
                verticies = line.split(',')
            else:
                tuple_line = self.line_to_tuple(line)
                edges.append(tuple_line)
                if directional is False:
                    edges.append((tuple_line[1], tuple_line[0], tuple_line[2]))
        f.close()
        return verticies, edges

    def read_from_d(self, f):
        pass

    def line_to_tuple(self, line):
        stack = []
        start = True
        for char in line:
            if char == '(' or char == ')':
                continue
            elif char == ',':
                start = True
            else:
                if start:
                    stack.append(char)
                    start = False
                else:
                    stack.append(stack.pop() + char)
        return tuple(stack)
