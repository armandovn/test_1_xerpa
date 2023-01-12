import unittest

from aritmetic_module.aritmetic_operations import *

class TestOperatorMethods(unittest.TestCase):

    def test_times(self):
        self.assertEqual(four(times(five())), 20)
    
    def test_plus(self):
        self.assertEqual(four(plus(five())), 9)
    
    def test_minus(self):
        self.assertEqual(five(minus(five())), 0)
    
    def test_divided_by(self):
        self.assertEqual(one(divided_by(one())), 1)
    
    def test_operation_1(self):
        self.assertEqual(four(times(five())), 20)
    
    def test_operation_2(self):
        self.assertEqual(one(plus(eight())), 9)
    
    def test_operation_3(self):
        self.assertEqual(seven(minus(three())), 4)
    
    def test_operation_4(self):
        self.assertEqual(nine(divided_by(three())), 3)


class TestNumberMethods(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(zero(), 0)

    def test_one(self):
        self.assertEqual(one(), 1)
    
    def test_two(self):
        self.assertEqual(two(), 2)
    
    def test_three(self):
        self.assertEqual(three(), 3)
    
    def test_four(self):
        self.assertEqual(four(), 4)
    
    def test_five(self):
        self.assertEqual(five(), 5)
    
    def test_six(self):
        self.assertEqual(six(), 6)
    
    def test_seven(self):
        self.assertEqual(seven(), 7)
    
    def test_eight(self):
        self.assertEqual(eight(), 8)
    
    def test_nine(self):
        self.assertEqual(nine(), 9)


if __name__ == '__main__':
    unittest.main()