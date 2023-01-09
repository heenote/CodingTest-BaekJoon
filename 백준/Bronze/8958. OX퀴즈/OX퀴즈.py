X = int(input())
for _ in range(X):
  Y = list(input())
  a= 0
  A = []
  for j in Y:
     if(j =='O'):
      a = a + 1
      A.append(a)
     else:
      a = 0
  print(sum(A)) 