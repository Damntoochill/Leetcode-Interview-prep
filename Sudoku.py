values = [[0,9,0,0,8,3,0,0,0],
          [0,0,0,9,0,0,0,0,7],
          [0,0,8,0,0,0,0,1,0],
          [2,0,0,0,6,4,0,0,0],
          [0,3,0,0,0,0,0,0,0],
          [0,0,0,1,0,2,0,7,0],
          [0,2,0,0,0,0,3,4,0],
          [0,5,0,0,4,0,0,2,0],
          [0,0,0,0,0,6,0,0,1]]

def empty_finder(values):
  for i in range(9):
    for j in range(9):
      if values[i][j] == 0 :
        return (i,j)
  return None

def validator(values, num, pos):
  #check num is valid in Row
  for i in range(9):
    #we check only 8 positions leaving pos[i][j]
    if values[pos[0]][i] == num and pos[1]!= i:
      return False
  #check num is valid in column
  for i in range(9):
    if values[i][pos[1]] == num and pos[0]!=i:
      return False
  #check num is valid in a square
  #indexing the squares
  square_x = pos[0]//3
  square_y = pos[1]//3
  for i in range(square_x*3, square_x*3 + 3):
    for j in range(square_y*3, square_y*3 + 3):
      if values[i][j] == num and (i,j) != pos:
        return False
  
  return True
    


def board_printer(values):
  for i in range(len(values)):
    if i %3 == 0 and i!=0:
      print('------------------------')
    for j in range(len(values)):
      if j%3 == 0 and j!=0:
        print(' | ', end = "")
      #print(values[i][j], end = "")
      if j == 8:
        print(values[i][j])
      else:
        print(str(values[i][j]) + " ", end = "" )

#board_printer(values)
#print( values[0])

def solve(values):
  print(values)
  find = empty_finder(values)
  if not find:
    return True
  else:
    row, col = find
  
  for i in range(1,10):
    if validator(values, i, find):
      values[row][col] = i

      if solve(values):
        return True
      else:
        values[row][col] = 0
  return False

board_printer(values)
print('\n\n')
solve(values)
board_printer(values)
    
