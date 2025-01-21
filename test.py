import unittest
from main import recursive_distance


class Test1(unittest.TestCase):
    def test_function(self):
        '''
        Here we'll test same one-letter string
        '''
        data1 = "c"
        data2 = "c"
        result = recursive_distance(data1, data2)
        self.assertEqual(0, result)

class Test2(unittest.TestCase):
    def test_function(self):
        '''
        Here we'll test the case of more letters but one different in the inputs
        '''
        data1 = "casa"
        data2 = "cara"
        result = recursive_distance(data1, data2)
        self.assertEqual(1, result)

class Test3(unittest.TestCase):
    def test_function(self):
        '''
        Here we'll test the case of more different letters in the inputs
        '''
        data1 = "cassa"
        data2 = "rasta"
        result = recursive_distance(data1, data2)
        self.assertEqual(2, result)

class Test4(unittest.TestCase):
    def test_function(self):
        '''
        Here we'll test the case of no letters in the inputs
        '''
        data1 = ""
        data2 = ""
        result = recursive_distance(data1, data2)
        self.assertEqual(0, result)