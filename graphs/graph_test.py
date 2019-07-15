from graph import Vertex, ADTGraph, FileReader
import unittest

class VertexTest(unittest.TestCase):
    def test_init(self):
        vert = Vertex(1)
        assert vert.data is 1
        assert vert.pointers.size is 0

    def test_points_to(self):
        vert1 = Vertex(1)
        vert2 = Vertex(2)
        assert vert1.is_pointing_to(vert2) is False
        assert vert1.pointers.size == 0
        vert1.points_to(vert2)
        assert vert1.is_pointing_to(vert2) is True
        assert vert2.is_pointing_to(vert1) is False
        assert vert1.pointers.size == 1
        vert3 = Vertex(3)
        vert1.points_to(vert3)
        vert2.points_to(vert1)
        assert vert1.pointers.size == 2
