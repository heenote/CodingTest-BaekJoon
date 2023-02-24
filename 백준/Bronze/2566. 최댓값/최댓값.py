A =[]
farr = list(list(map(int,input().split()))for _ in range(9))
for i in farr:
 A.append(max(i))
print(max(A))
for i in range(len(farr[0])):
 for j in range(9):
  if farr[i][j] == max(A): 
   print(i+1, j+1)
   break