""" linked_list.py

Student: Anna Enerud
Mail: anna.enerud.3261@student.uu.se
Reviewed by: Andreas Pihl
Date reviewed: 28/4-2023
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):       # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):      # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):             # Optional
        f = self.first
        n = 0
        while f:
            n += 1
            f = f.succ
        return n

    def mean(self):               # Optional
        sum = 0
        f= self.first
        while f:
            sum += f.data
            f = f.succ
        return sum/LinkedList.length(self)

    def remove_last(self):        # Optional
        if self.first == None: #tomma listor
            raise ValueError("Empty list")
        f = self.first
        if self.first.succ == None: #om listan bara har ett element
            res = f.data
            self.first = None
        else:
            while f.succ.succ: #stannar på näst sista elementet
                f = f.succ
            res = f.succ.data
            f.succ = None #ingen pekare till sista elementet
        return res

    def remove(self, x):          # Compulsory
        f = self.first
        if self.first == None: #går ej att ta bort från tom lista
            return False
        elif self.first.data == x: #om första elementet ska tas bort kan vi hantera det direkt
            self.first = self.first.succ
            return True
        else:
            while f.succ:
                if f.succ.data == x:
                    f.succ = f.succ.succ #vill peka till elementet efter det som ska tas bort
                    return True
                f = f.succ
            return False

    def count(self, x):           # Optional
        return self._count(x, self.first)

    def _count(self,x, f):
        if f is None:
            return 0
        elif f.data != x:
            return self._count(x, f.succ)
        else:
            return 1 + self._count(x, f.succ)


    def to_list(self):            # Compulsory
        return self._to_list(self.first)

    def _to_list(self,f): #hjälpmetod
        if f is None:
            return []
        else:
            return [f.data] + self._to_list(f.succ)

    def remove_all(self, x):  # Compulsory
        def _remove(x, f):
            if f is None:
                return 0
            if f.data == x:
                self.remove(x) #tar bort x ur listan (som består av ett element)
                return 1 + _remove(x, f.succ)
            else:
               return _remove(x, f.succ)
        return _remove(x, self.first)


    def __str__(self):            # Compulsary
        result = '('
        n = 0
        for x in self:
            if n < self.length() - 1:
                result += str(x) + ', '
            else:
                result += str(x)
            n += 1
        return  result + ')'

   # def copy(self):               # Compulsary
    #    result = LinkedList()
    #    for x in self:
     #       result.insert(x)
      #  return result
    '''' Complexity for this implementation: 
        I copy gås hela listan igenom och i iter gås också hela listan igenom för varje element
        så om vi lägger till ett element till i listan måste alla tidigare element också gås igenom 
        komplexiteten blir alltså O(n^2)
    '''

    def copy(self): # Compulsary
        result = LinkedList()
        py_list = self.to_list()
        rev_py_list = reversed(py_list)
        for x in rev_py_list:
            result.insert(x)
        return result
    ''' Complexity for this implementation:
        to_list går igenom varje element en gång. Om vi kör insert på listan från störst till minst behöver varje
        element bara en beräkning dvs tiden ökar linjärt med antal element. Komplexiteten är O(n)
    '''

    def __getitem__(self, ind):   # Optional
        if ind >= self.length():
            raise IndexError
        else:
            f = self.first
            for i in range(ind):
                f = f.succ
            return f.data

class Person:                     # Compulsory
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __le__(self, other):
        if self.name <= other.name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.name < other.name:
            return True
        else:
            return False


def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()
    print(lst)
    lst2 = LinkedList()
    lst2.insert(3)
    print(lst2)

    # Test code:
    plist = LinkedList()
    p = Person('Niki', 199805106634)
    plist.insert(p)
    q = Person('Anna', 200101010101)
    plist.insert(q)
    print(plist)


if __name__ == '__main__':
    main()
