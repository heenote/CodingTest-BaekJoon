X = list(map(int,(input().split())))
if X[1] >= X[2]: 
  print(-1) 
else: print(X[0]//(X[2] - X[1])+1)