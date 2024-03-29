from vertex import Vertex
import unittest


class VertexTest(unittest.TestCase):
    def test_init(self):
        vert = Vertex(1)
        assert vert.data is 1
        assert len(vert.neighbors) == 0

    def test_points_to(self):
        one = Vertex('one')
        two = Vertex('two')
        one.points_to(two)
        two.points_to(one)
        assert len(one.neighbors) == 1
        assert len(two.neighbors) == 1

    def test_is_pointing_to(self):
        one = Vertex('one')
        two = Vertex('two')
        one.points_to('two')
        two.points_to('one')
        assert one.is_pointing_to('two') is True
        assert two.is_pointing_to('one') is True
        assert one.is_pointing_to('three') is False
