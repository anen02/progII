"""
Unittests for the binary search tree methods
"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):

    def test_remove(self):
        bst = BST()
        lst = LinkedList()
        for x in [5, 3, 8, 1, 4, 6, 9, 10]:
            bst.insert(x)
            lst.insert(x)

        print('\nTests BST remove')
        for x in [9, 10, 5, 3, 4, 6, 8, 1, 1]:
            self.assertEqual(bst.remove(x), bst.root)
            lst.remove(x)
            self.assertEqual(str(bst.to_LinkedList()), str(lst))
        self.assertEqual(bst.root, None)




if __name__ == "__main__":
    unittest.main()
