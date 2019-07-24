#!python


class Vertex(object):
    def __init__(self, data: str):
        self.data = data
        self.pointers = dict()

    def points_to(self, pointer, weight=1):
        '''Adds a pointer to the linked list of pointers'''
        self.pointers[pointer] = weight

    def is_pointing_to(self, item: str):
        '''returns a boolean indicating whether the vertex is pointing to another item'''
        return item in self.pointers
