# ex-5.5.py
# Andy Mina
# CSCI 77800 Fall 2023

def draw(t, length, n):
  """
  Draws a spiral fractal with decreasing side lengths on each sub-fractal.
  """
  if n == 0:
    return
  angle = 50
  fd(t, length * n)
  lt(t, angle)
  draw(t, length, n - 1)
  rt(t, 2 * angle)
  draw(t, length, n - 1)
  lt(t, angle)
  bk(t, length * n)