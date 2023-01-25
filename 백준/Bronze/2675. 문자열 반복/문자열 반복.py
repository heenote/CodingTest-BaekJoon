num = int(input())
for _ in range(0,num):
  Y = ''
  X = input().split()
  for j in X[1]:
    Y += '' + (j * int(X[0]))
  print(Y)