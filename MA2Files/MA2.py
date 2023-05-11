"""
Solutions to module 2 - A calculator
Student: Anna Enerud
Mail: anna.enerud.3261@student.uu.se
Reviewed by: Elis Pettersson Gradin
Reviewed date: 14/4
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

from MA2tokenizer import TokenizeWrapper
import math
from tokenize import TokenError


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if wtok.is_at_end():  #EOL
        return result
    else:
        raise SyntaxError(": Invalid expression")


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if not wtok.is_name():
            raise SyntaxError(": Assignment must be to names")
        else:  #add to the variables dictionary
            variables[wtok.get_current()] = result
            wtok.next()
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        else:
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/' or wtok.get_current() == '%':
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)

        else:
            wtok.next()
            div = factor(wtok, variables)
            if div != 0:  #check for division with 0
                result = result/div
            else:
                raise EvaluationError(': Division by zero')
    return result


def factor(wtok, variables):
    """ See syntax chart for factor
        Follow the syntax chart as closely as possible!
        Check only for syntax error - not for evaluation errors!
    """

    FUNCTIONS_1 = {'sin': sin, 'cos': cos, 'exp': exp, 'log': log, 'fib': fib, 'fac': fac}
    FUNCTIONS_N = {'min': min, 'max': max, 'sum': sum, 'mean': mean}

    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError(": Expected ')'")
        else:
            wtok.next()

    elif wtok.get_current() in FUNCTIONS_1:
        func = FUNCTIONS_1[wtok.get_current()]
        wtok.next()
        if wtok.get_current() == '(':
            result = func(factor(wtok, variables))  #if assignment is called sin(PI+1)= sin(PI) + 1
        else:
            raise SyntaxError(": Expected '('")

    elif wtok.get_current() in FUNCTIONS_N:
        func = FUNCTIONS_N[wtok.get_current()]
        wtok.next()
        result = func(arglist(wtok, variables))  #arglist checks for ()

    elif wtok.get_current() in variables:
        numb = TokenizeWrapper(str(variables.get(wtok.get_current())))  #must use a tokenizer object
        result = assignment(numb, variables)
        wtok.next()

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok, variables)

    elif wtok.is_name():  #kollar redan om det är funktion eller variabel
        raise EvaluationError(f': Undefined variable: "{wtok.get_current()}"')

    else:
        raise SyntaxError(": Expected number, word or '('")

    return result


def arglist(wtok, variables):
    if wtok.get_current() == '(':
        res = []
        wtok.next()
        res.append(assignment(wtok, variables))

        while wtok.get_current() == ',':
            wtok.next()
            res.append(assignment(wtok, variables))

        if wtok.get_current() != ')':
            raise SyntaxError(": Expected ')' or ','")
        else:
            wtok.next()
            return res
    else:
        raise SyntaxError(": Expected '('")


def sin(x):
    if x == math.pi:
        return 0
    else:
        return math.sin(x)


def cos(x):
    return math.cos(x)


def exp(x):
    return math.exp(x)


def log(x):
    if x <= 0:
        raise EvaluationError(f': Illegal value: log({x}) is not defined¨')
    else:
        return math.log(x, math.e)


def fib(n):
    """Jag använde en iterativ metod pga man kunde inte räkna så stora tal som jag ville kunna
    med rekursion (även om man använde sig av memoization) pga rekursionsdjupet"""
    if n != int(n) or n <= 0:
        raise EvaluationError(f': Argument to fib is {n}, argument must be integer larger than 0')

    res = [0, 1] + [None for i in range(int(n-1))]
    for i in range(int(n-1)):
            res[i + 2] = res[i] + res[i + 1]
    return res[-1]


def fac(n):  #med rekursion kan man inte räkna tal större än ca 1000 pga rekursionsdjup
    if n != int(n) or n <= 0:
        raise EvaluationError(f': Argument for fac is {n}, argument must be integer larger than 0')

    else:
        res = 1
        for x in range(1, int(n+1)):
            res = res*x
    return res


def mean(arglist):
    return sum(arglist)/len(arglist)


def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file.

    You need to add handling of EvaluationError in this function!
    """

    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0] == '#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            for i, key in enumerate(variables):
                print(f' {key} :\t {variables[key]}')
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError:
                print('*** Syntax error: Unbalanced parentheses')

            except EvaluationError as ee:
                print("*** Evaluation error", ee)


if __name__ == "__main__":
    main()
