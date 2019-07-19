from graph import ADTGraph
import unittest


class GraphTest(unittest.TestCase):
    def test_init(self):
        path = 'file_reader_test.txt'
        g = ADTGraph(path)
        assert g.all_verticies == ['1', '2', '3', '4', '5']
        assert g.edges == [('1', '2'), ('2', '1'), ('2', '3'), ('3', '2'), ('3', '4'), ('4', '3'),
                           ('4', '5'), ('5', '4'), ('5', '1'), ('1', '5')]
        assert g.vertex_count == 5
        assert g.edge_count == 10
