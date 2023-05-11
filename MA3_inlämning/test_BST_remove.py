"""
Unittests for the binary search tree methods
"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):

    def test_remove(self):
        print('\nTests BST remove')
        bst = BST()
        lst = LinkedList()
        for x in [12, 5, 23, 2, 8, 17, 13, 36, 42, 7, 6, 21, 14]:
            bst.insert(x)
            lst.insert(x)
        print(bst.__str__())
        self.assertEqual(bst.__str__(), '<2, 5, 6, 7, 8, 12, 13, 14, 17, 21, 23, 36, 42>')
        bst.remove(2)
        lst.remove(2)
        self.assertEqual(bst.__str__(), '<5, 6, 7, 8, 12, 13, 14, 17, 21, 23, 36, 42>')
        bst.remove(17)
        lst.remove(17)
        self.assertEqual(bst.__str__(), '<5, 6, 7, 8, 12, 13, 14, 21, 23, 36, 42>')
        for x in [12, 5, 23, 8, 13, 36, 42, 7, 6, 21, 14]:
            print('Node:', x)
            lst.remove(x)
            self.assertEqual(bst.remove(x), bst.root)
            self.assertEqual(str(bst.to_LinkedList()), str(lst))

        # for x in [6, 13, 23]:
        # print(bst.to_LinkedList())
        # self.assertEqual(bst.remove(x), bst.root)
        # print(lst)
        # lst.remove(x)
        # print(lst)
        # print(bst.to_LinkedList())
        # self.assertEqual(str(bst.to_LinkedList()), str(lst))
        # self.assertEqual(bst.root, None)

    def _test_remove(self):
        bst = BST()
        lst = LinkedList()
        for x in [5, 3, 8, 1, 4, 6, 9, 10]:
            bst.insert(x)
            lst.insert(x)

        print('\nTests BST remove')
        for x in [9, 8, 10, 5, 3, 4, 6, 1, 1]:
            self.assertEqual(bst.remove(x), bst.root)
            lst.remove(x)
            self.assertEqual(str(bst.to_LinkedList()), str(lst))
        self.assertEqual(bst.root, None)




if __name__ == "__main__":
    unittest.main()
