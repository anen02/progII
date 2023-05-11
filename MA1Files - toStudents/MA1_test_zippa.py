# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_zippa(self):
        print('\nTests zippa')
        res = zippa([], [])
        self.assertEqual(res, [])
        res = zippa([1,2,3],[])
        self.assertEqual(res, [1,2,3])
        res = zippa(['a' , 1, 3], ['b', 2, 4])
        self.assertEqual(res, ['a', 'b', 1, 2, 3, 4])
        res = zippa([1, 3, 5, 7, 9], [2, 4])
        self.assertEqual(res, [1, 2, 3, 4, 5, 7, 9])
        res = zippa(['a', 'c'], ['b', 'd', 'e', 'f'])
        self.assertEqual(res, ['a', 'b', 'c', 'd', 'e', 'f'])



if __name__ == "__main__":
    unittest.main()
