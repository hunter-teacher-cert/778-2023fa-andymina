# GOL
# Andy Mina
# CSCI 77800 Fall 2023
ALIVE_CHAR = 'X'
DEAD_CHAR = ' '
ROWS = 10
COLS = 10

def printBoard(board):
  for row in board:
      print(','.join(row))

  print()
  print('-' * COLS * 2)

def createNewBoard(rows, cols):
  board = [[DEAD_CHAR] * cols for _ in range(rows)]
  return board

def countNeighbors(board, row, col):
  adj_alive = 0

  for row_modifier in range(-1, 2):
    for col_modifier in range(-1, 2):
      if (row_modifier == 0 and col_modifier == 0):
        continue
      
      neighborRow = row + row_modifier
      neighborCol = col + col_modifier

      rowInBounds = neighborRow >= 0 and neighborRow < len(board)
      colInBounds = neighborCol >= 0 and neighborCol < len(board[0])

      if (rowInBounds and colInBounds and board[neighborRow][neighborCol] == ALIVE_CHAR):
        adj_alive += 1
  
  return adj_alive

def getNextGenCell(board, row, col):
  adj_alive = countNeighbors(board, row, col)
  return ALIVE_CHAR if (adj_alive == 2 and board[row][col] == ALIVE_CHAR) or (adj_alive == 3) else DEAD_CHAR

def generateNextBoard(board):
  next_gen = createNewBoard(len(board), len(board[0]))

  for row in range(len(board)):
    for col in range(len(board[row])):
      next_gen[row][col] = getNextGenCell(board, row, col)

  return next_gen

def setWalking(board):
  board[0][1] = ALIVE_CHAR
  board[1][2] = ALIVE_CHAR
  board[2][0] = ALIVE_CHAR
  board[2][1] = ALIVE_CHAR
  board[2][2] = ALIVE_CHAR  

def main():
  maxGens = 10
  gen = 0
  board = createNewBoard(ROWS, COLS)

  setWalking(board)
  printBoard(board)
  while (gen < maxGens):
    board = generateNextBoard(board)
    printBoard(board)
    gen += 1

main()