class FileReader(object):
    def __init__(self, PATH = None):
        self.PATH = PATH
    
    def read_from_g(self):
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