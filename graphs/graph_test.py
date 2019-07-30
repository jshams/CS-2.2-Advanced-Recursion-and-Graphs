from graph import ADTGraph
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class GraphTest(unittest.TestCase):
    def test_init(self):
        path = 'file_reader_test.txt'
        g = ADTGraph(path)
        self.assertCountEqual(g.vertices.keys(), ['1', '2', '3', '4', '5'])
        egde_list = [('1', '2'), ('2', '3'),  ('3', '4'),
                     ('4', '5'),  ('5', '1')]
        self.assertCountEqual(g.edges, egde_list)
        assert g.vertex_count == 5
        assert g.edge_count == 5
        assert g.vertices['1'].is_pointing_to('2') is True

    def test_add_vertex(self):
        g = ADTGraph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        assert g.vertex_count == 3
        assert len(g.vertices) == 3
        self.assertCountEqual(g.vertices.keys(), [1, 2, 3])

    def test_add_edge(self):
        g = ADTGraph()
        g.add_verticies([1, 2, 3])
        g.add_edge(1, 2, 3)
        g.add_edge(2, 1, 3)
        g.add_edge(3, 2, 1)
        g.add_edge(2, 3, 1)
