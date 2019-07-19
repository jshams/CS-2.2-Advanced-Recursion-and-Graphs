from file_reader import FileReader
import unittest


class FileReaderTest(unittest.TestCase):
    def test_init(self):
        path = 'file_reader_test.txt'
        f = FileReader(path)
        assert f.PATH == 'file_reader_test.txt'

    def test_line_to_tuple(self):
        path = 'file_reader_test.txt'
        assert FileReader(path).line_to_tuple('(12,24)') == ('12', '24')
        assert FileReader(path).line_to_tuple(
            '(12,24,36)') == ('12', '24', '36')
        assert FileReader(path).line_to_tuple(
            '(12,24,36,48)') == ('12', '24', '36', '48')

    def test_read_file(self):
        path = 'file_reader_test.txt'
        f = FileReader(path)
        verticies, edges = f.read_file()
        assert verticies == ['1', '2', '3', '4', '5']
        assert edges == [('1', '2'), ('2', '1'), ('2', '3'), ('3', '2'), ('3', '4'), ('4', '3'),
                         ('4', '5'), ('5', '4'), ('5', '1'), ('1', '5')]
