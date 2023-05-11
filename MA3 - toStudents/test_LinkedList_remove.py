
"""
Unittests for the linked lists remove
"""

import unittest

from linked_list import *


class Test(unittest.TestCase):

    def test_remove(self):
        print('\nTests remove')
        lst = LinkedList()
        for x in [3, 1, 2, 6]:
            lst.insert(x)

        self.assertEqual(lst.remove(9), False)
        self.assertEqual(lst.remove(3), True)
        self.assertEqual(lst.remove(6), True)
        self.assertEqual(lst.remove(6), False)
        self.assertEqual(lst.remove(1), True)
        self.assertEqual(lst.remove(2), True)
        self.assertEqual(lst.remove(2), False)
        lst2 = LinkedList()
        self.assertEqual(lst2.remove(2), False)




    

if __name__ == "__main__":
    unittest.main()
