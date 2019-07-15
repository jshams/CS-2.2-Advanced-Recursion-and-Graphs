from file_reader import FileReader
import unittest

class FileReaderTest(unittest.TestCase):
    def test_init(self):
        f = FileReader('PATH')
        assert f.PATH == 'PATH'
    
    def test_line_to_tuple(self):
        assert FileReader().line_to_tuple('(12,24)') == ( '12','24')
        assert FileReader().line_to_tuple('(12,24,36)') == ( '12','24','36')
        assert FileReader().line_to_tuple('(12,24,36,48)') == ( '12','24','36','48')
