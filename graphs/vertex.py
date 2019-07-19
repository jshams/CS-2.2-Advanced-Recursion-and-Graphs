from linkedlist import LinkedList


class Vertex(object):
    def __init__(self, data: str):
        self.data = data
        self.pointers = LinkedList()

    def points_to(self, pointer, weight=1):
        '''Adds a pointer to the linked list of pointers'''
        self.pointers.append((pointer, weight))

    def is_pointing_to(self, item: str):
        '''returns a boolean indicating whether the vertex is pointing to another item'''
        for vert in self.pointers:
            if vert[0].data == item:
                return True
        return False
