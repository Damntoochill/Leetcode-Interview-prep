matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
l,r,t,b = 0, len(matrix[0])-1,0, len(matrix)-1
print(l,r,t,b)
r_matrix = []
direction = 0
#j = 1
while(l<=r and t<=b):
  if direction == 0:
    for i in range(l,r+1):
      print(matrix[t][i])
    #direction = 1
    t += 1
  elif direction == 1:
    for i in range(t,b+1):
      #print(t,b+1)
      print(matrix[i][r])
    #direction = 2
    r -= 1
  elif direction == 2:
    for i in range(r,l-1,-1):
      print(matrix[b][i])
   # direction = 3
    b -= 1
  elif direction == 3:
    for i in range(b,t-1,-1):
      print(matrix[i][l])
    #direction = 4
    l += 1
  direction = (direction +1)% 4



#while():
 # if(direction == 0):
  #  for i in range(r+1):
   #   r_matrix.append(matrix[l][i])

  
