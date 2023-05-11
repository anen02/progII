""" bst.py

Student: Anna Enerud
Mail: anna.enerud.3261@student.uu.se
Reviewed by: Andreas Pihl
Date reviewed: 28/4-2023
"""

from linked_list import LinkedList
import random
import math


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        return self._height(self.root)

    def _height(self, r):
        heights = []
        if r is None:
            heights.append(0)  # basfall
        else:
            heights.append(1 + self._height(r.left))  # lägger till höjderna för varje subträd i listan
            heights.append(1 + self._height(r.right))
        return max(heights)  # det längsta avståndet är höjden

    def __str__(self):                            # Compulsory
        result = '<'
        n = 0
        for x in self:
            if n < self.size()-1:
                result += str(x) + ', '
                n += 1
            else:
                result += str(x)
        return result + '>'

    def to_list(self):                            # Compulsory
        return self._to_list(self.root)

    def _to_list(self, r):
        if r is None:
            return []
        else:
            return self._to_list(r.left) + self._to_list(r.right) + [r.key]
    """O(n) (vi går igenom varje subträd (varje nod) en gång)"""

    def to_LinkedList(self):                      # Compulsory
        lst = LinkedList()

        def _to_LinkedList(lst, r):
            if r is not None:
                if r.right is not None:  # lägg in från största till minsta
                    _to_LinkedList(lst, r.right)
                    lst.insert(r.right.key)
                if r.left is not None:
                    _to_LinkedList(lst, r.left)
                    lst.insert(r.left.key)
            return lst

        _to_LinkedList(lst, self.root)

        if self.root is not None:
            lst.insert(self.root.key)  # lägg in roten sist (kommer behöva gå igenom ca halva listan igen)
        return lst
    """Från testerna: dubbelt antal noder ger dubbelt så lång tid dvs, metoden är O(n)"""

    def remove(self, key):
        self.root = self._remove(self.root, key)
        return self.root

    def _remove(self, r, k):  # Compulsory
        """"Troligtvis i en väldigt tillkrånglad variant"""

        def smallest_key(r):  # returnerar noden med minsta nyckeln
            if r.left is not None:
                return smallest_key(r.left)
            else:
                return r

        if r is None:
            return None
        elif k < r.key:  # tar bort k ur vänstra subträdet
            if r.left is not None:
                if k == r.left.key:
                    if r.left.right and r.left.left is not None:  # då är vi i fallet med två barn
                        r.left = self._remove(r.left, k)  # kör remove på vänster subträd
                    elif r.left.right is not None:
                        r.left = r.left.right
                    else:
                        r.left = r.left.left
                r.left = self._remove(r.left, k)
        elif k > r.key:  # lika som tidigare fast för höger subträd
            if r.right is not None:
                if k == r.right.key:
                    if r.right.right and r.right.left is not None:
                        r.right = self._remove(r.right, k)
                    elif r.right.right is not None:
                        r.right = r.right.right
                    else:
                        r.right = r.right.left
                r.right = self._remove(r.right, k)
        else:  # This is the key to be removed
            if r.left is None:  # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                smallest = smallest_key(r.right)  # minsta noden i höger subträd sparas
                self._remove(r, smallest.key)  # ta bort den minsta noden
                r.key = smallest.key  # byt ut den noden som man vill ta bort mot den minsta i höger subträd

        return r  # returnerar roten i nuvarande träd

    def ipl(self):  # Compulsory
        heights = []
        lvl = 1

        def _ipl(r, level):
            level += 1
            if r.right is not None:
                heights.append(level)
                _ipl(r.right, level)
            if r.left is not None:
                heights.append(level)
                _ipl(r.left, level)
            return heights

        if self.root is not None:
            heights.append(lvl)
            return sum(_ipl(self.root, lvl))
        else:
            return 0


def random_tree(n):  # Useful
    random_t = BST()
    for i in range(n):
        random_t.insert(random.random())
    return random_t


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")


    for i in [10, 100, 1000, 10000, 100000]:
        r_tree = random_tree(i)
        print(f'antal noder: {i}')
        print(f'Nodhöjd {r_tree.ipl()/i}')
        print(f'Höjd {r_tree.height()} ')
        print(f'Factor: {((r_tree.ipl()/i)/math.log(i, 2))}')


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size?
Då man ändå måste gå igenom hela trädet för att se hur stort det är kan man använda generatorn för att göra detta
2. computing height?
Här måste vi kolla varje möjlig väg från rot till löv så generatorn blir inte så användbar
3. contains?
Den kan bli lättare att förstå om man använder generatorn, själva koden blir kortare. Men man tappar de bra 
sökegenskaperna hoss binära sökträd eftersom att man med generatorn går igenom alla nycklar tills man hittat den
man vill ha men med den metoden som finns nu faktiskt använder sökträdsegenskaperna för att gå via så få noder som
möjligt
4. insert?
Det blir samma som för contains, man tappar fördelarna med ett sökträd. Dessutom hatr inte generatorn koll på trädstrukturen
så det går inte riktigt.
5. remove?
Detta blir också liknande, man tappar några av fördelarna i hur man hittar noden som ska tas bort (snabb sökning),
men man behöver fortfarande hantera alla specialfall. Generatorn har ingen koll på strukturen.




Results for ipl of random trees
===============================
Factor blir ungefär 1.39 (närmare för större antal noder men för många noder ger hög beräkningstid)
Höjden av trädet blir (kanske uppenbart) större med antalet noder, från instruktionerna vet vi att minsta möjliga
höjd för ett träd med n noder är log_2(n). Men om vi tittar på vilka höjder vi faktiskt får ser det ut som att den
ökar med ca 10 för varje faktor 10 vi ökar antalet noder med. Vi får en ungefärlig formel h(n) = 10*log_10(n) - 10,
logaritmisk ökning.



"""
