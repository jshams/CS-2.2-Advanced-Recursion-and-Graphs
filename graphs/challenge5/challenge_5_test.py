from challenge_5 import has_eulerian_cycle, read
import unittest


class FileReaderTest(unittest.TestCase):
    def test_read(self):
        path = 'graph_data.txt'
        edge_list = read(path)
        assert edge_list == [('1', '2'), ('2', '3'), ('3', '4'),
                             ('4', '5'), ('1', '5')]

    def test_has_eulerian_cycle(self):
        edge_list = [('1', '2')]
        assert has_eulerian_cycle(edge_list) == False
        edge_list = [('1', '2'), ('2', '3'), ('3', '1')]
        assert has_eulerian_cycle(edge_list) == True
        edge_list = [('1', '2'), ('2', '3'), ('3', '1'), ('3', '4')]
        assert has_eulerian_cycle(edge_list) == False
        edge_list = [('1', '2'), ('2', '3'), ('3', '4'),
                     ('4', '5'), ('1', '5')]
        assert has_eulerian_cycle(edge_list) == True
