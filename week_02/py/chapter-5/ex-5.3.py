# ex-5.3.py
# Andy Mina
# CSCI 77800 Fall 2023

def check_fermat(a, b, c, n):
    lhs = a ** n  + b ** n
    rhs = c ** n
    if (n > 2 and lhs == rhs):
        print('Holy smokes, Fermat was wrong')
    else:
        print('No, that doesn\'t work')

def prompt_frmat():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    n = int(input('Enter n: '))

    check_fermat(a,b,c,n)