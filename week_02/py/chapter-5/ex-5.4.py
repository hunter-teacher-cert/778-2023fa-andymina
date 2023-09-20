# ex-5.4.py
# Andy Mina
# CSCI 77800 Fall 2023

def is_triangle(a, b, c):
  if (a + b > c or b + c > a or a + c > b):
    print('No')
  else:
    print('Yes')

def prompt_triangle(a, b, c):
  a = int(input('Enter a: '))
  b = int(input('Enter b: '))
  c = int(input('Enter c: '))

  is_triangle(a, b, c)