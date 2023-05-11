# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_count(self):
        print('\nTests count')
        res = count(4, [1, [ 4, 4 ] , 3, 1, 4, 2, ['a', [ [ 4, 4 ] , 4, 4] ] ] )
        self.assertEqual(res, 7)
        res = count(1,[])
        self.assertEqual(res, 0)
        res = count(1, [1,2,1])
        self.assertEqual(res,2)
        res = count([1, 2], [1, [1, 2]])
        self.assertEqual(res, 1)
        res = count([3,2], [[[3,2], 3, [3,2]]])
        self.assertEqual(res, 2)



if __name__ == "__main__":
    unittest.main()
