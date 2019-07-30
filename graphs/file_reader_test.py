from file_reader import FileReader
import unittest


class FileReaderTest(unittest.TestCase):
    def test_init(self):
        path = 'file_reader_test.txt'
        f = FileReader(path)
        assert f.PATH == 'file_reader_test.txt'
        assert len(f.edges) > 0
        assert len(f.verticies) > 0

    def test_is_digraph(self):
        path = 'file_reader_test.txt'
        f = FileReader(path)
        assert f.PATH == 'file_reader_test.txt'
        assert f.digraph == False

    def test_line_to_tuple(self):
        f = FileReader()
        assert f.line_to_tuple('(12,24)') == ('12', '24')
        assert f.line_to_tuple(
            '(12,24,36)') == ('12', '24', '36')
        assert f.line_to_tuple(
            '(12,24,36,48)') == ('12', '24', '36', '48')

    def test_read_file(self):
        path = 'file_reader_test.txt'
        f = FileReader(path)
        assert f.verticies == ['1', '2', '3', '4', '5']
        assert f.edges == [('1', '2'), ('2', '3'),
                           ('3', '4'), ('4', '5'),  ('5', '1')]
