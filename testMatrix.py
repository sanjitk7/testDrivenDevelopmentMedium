import unittest
from matrixOperations import add,multiply

class TestMatrix(unittest.TestCase):
    def test_add(self):
        A = [[1,1,1],[1,1,1],[1,1,1]]
        B = [[1,1,1],[1,1,1],[1,1,1]]
        sum = [[2,2,2],[2,2,2],[2,2,2]]
        self.assertEqual(add(A,B),sum)
        
    def test_multiply(self):
        A = [[1,1,1],[1,1,1],[1,1,1]]
        B = [[1,1,1],[1,1,1],[1,1,1]]
        product = [[3,3,3],[3,3,3],[3,3,3]]
        self.assertEqual(multiply(A,B),product)

