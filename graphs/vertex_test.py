from vertex import Vertex
import unittest

class VertexTest(unittest.TestCase):
    def test_init(self):
        vert = Vertex(1)
        assert vert.data is 1
        assert vert.pointers.size is 0

    def test_points_to(self):
        pass