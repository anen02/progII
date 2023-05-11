"""
Solutions to module 1
Student: Anna Enerud
Mail: anna.enerud.3261@student.uu.se
Reviewed by: Jens
Reviewed date: 23/3
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib functionen.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def power(x, n: int):                        # Optional
    """ Computes x**n using multiplications and/or division """
    res = 1 #basfall
    if n > 0: #rekursivdef
        res = x*power(x, n-1)
    elif n < 0: #om n negativ...
        res = 1/(x*power(x, -(n+1)))
    return res

def multiply(m: int, n: int) -> int:         # Compulsory
    """ Computes m*n using additions"""
    res = 0 #basfall n = 0
    if n > 0:
        res = m + multiply(m, n-1) #rekursiv definition, x*n = x*(n-1) + x
    return res

def divide(t: int, n: int) -> int:           # Optional
    """ Computes m*n using subtractions"""
    res = 0 #basfall
    if n > 0 and t >= n: #rekursiv def
        res = 1 + divide(t-n, n)
    return res

def harmonic(n: int) -> str:                 # Compulsory
    """ Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    res = 1 #basfall
    if n > 1: #h(n) = h(n-1) + 1/n är den rekursiva definitionen
        res = 1/n + harmonic(n-1)
    return res

def digit_sum(x: int, base=10) -> int:       # Optional #ej gjort
    """ Computes and returns the sum of the decimal (or other base) digits in x"""
    if x == 0:
        res = 0
    elif abs(x) < base:
        res = 1
    else:
        res = 1 + digit_sum(x//base)
    return res

def get_binary(x: int) -> str:               # Compulsary
    """ Returns the binary representation of x """
    if x == 0: #basfall
        res = '0'
    elif x == 1: #basfall
        res = '1'
    elif x > 1:
        res = get_binary(x//2) + get_binary(x%2)
        """ger antingen 0 eller 1 för största tvåpotensen i talet sedan "tas största tvåpotens bort" 
        m.h.a heltalsdivision och processen upprepas"""
    elif x < 0: #om negativt tal gör som för positivt och lägg på minus
        res = '-' + get_binary(-int(x))
    return res

def reverse_string(s: str) -> str:           # Optional
    """ Returns the s reversed """
    if len(s) <= 1: #basfall
        res = s
    else:
        n = len(s) - 1 #antal bokstäver i strängen
        res = reverse_string(s[n:]) + reverse_string(s[:n]) #tar de n sista bokstäverna i ordet i omvänd ordning
    return res

def largest(a: iter):                        # Compulsory
    """ Returns the largest element in a"""
    if len(a) == 1: #basfall
        res = a[0]
    else:
        n = len(a)//2 #vi vill dela listan i två delar
        if largest(a[:n]) > largest(a[n:]):
            """för varje steg väljer vi den lista som innehåller det största talet"""
            res = largest(a[:n])
        else:
            res = largest(a[n:])
    return res

def count(x, s: list) -> int:                # Compulsory
    """ Counts the number of occurences of x on all levels in s"""
    """Rekursionen går så vi utvidgar listan (typ)"""
    if len(s) > 0:
        if x != s[-1]:
            res = 0
        else:        #om sista elementet är x räkna en gång
            res = 1
        if type(s[-1]) == list:
            res = res + count(x, s[-1])
        res = res + count(x, s[:len(s)-1]) #upprepa tills vi gått igenom alla element
    else:
        res = 0
    return res


def zippa(l1: list, l2: list) -> list:       # Compulsory
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    n = max(len(l1), len(l2))
    m = min(len(l1), len(l2))
    if n <= 1: #basfall
        res = l1 + l2
    elif len(l1) != len(l2):
        """zippa den korta listan med den kortaste delen av den långa, addera resten av den långa listan"""
        res = zippa(l1[:m],l2[:m]) + l1[m:] + l2[m:]
    else:
        """om listorna är lika långa ska de zippas som vanligt (rekursion till basfallet)"""
        res = zippa(l1[:n-1], l2[:n-1]) + zippa(l1[n-1:], l2[n-1:])
    return res


def bricklek(f: str, t: str, h: str, n: int) -> str:  # Compulsory
    """ Returns a string of instruction how to move the tiles """
    if n >= 1: #kör flera gånger men byter plats på vilken som är start/slut torn
        return  bricklek(f,h,t, n-1) + [f + '->' + t] + bricklek(h,t,f, n-1)
    else: #basfall
        return []


def fib(n: int) -> int:                       # Compulsory
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    print('\nCode that demonstates my implementations\n')

    fib_numbers = [n for n in range(39)]
    times = [1]
    for i in fib_numbers: #tiderna för varje körning
        tstart = time.perf_counter()
        fib(i)
        tstop = time.perf_counter()
        print(f'Time for the {i}:th fibonacci number: {tstop-tstart}s')
        times.append(tstop-tstart)

    print(f'\nRelation between the time for 39:th and 38:th numbers {times[39]/times[38]}')
    print(f'c = t(n)/1.618^n')

    import statistics #räkna ut konstanten m.h.a medelvärdet för flera körningar
    c = []
    for i in range(33,39):
        c.append(times[i]/(1.618**i))
    c = statistics.mean(c)

    print(f'c is (approx): {c}')

    t_50 = c*1.618**50 #tiderna för det 50:e respektive 100:e talet
    t_100 = c*1.618**100
    print(f't(50): {round(t_50/60,0)}min')
    print(f't(100): {round(t_100/(60*60*24*365.25),0)}år')
    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  ca 35 000 000 år
  
  
  Exercise 17: Time for Fibonacci:
  50 tal: ca 28 min
  100 tal: ca 1 500 000 år
  
  
  Exercise 20: Comparison sorting methods:
  Instickssortering: 10^6: 11 år, 10^9: ca 32 000 år
  Mergesortering: 10^6: 34 min, 10^9: 35 dagar
  
                    
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  n < 10^10
  
  
  
  
  
  





"""
