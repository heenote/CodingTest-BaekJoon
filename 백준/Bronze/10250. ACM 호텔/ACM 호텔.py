X=int(input())
for _ in range(X):
 Y = input().split()
 F = int(Y[2]) % int(Y[0])
 S = (int(Y[2]) // int(Y[0])) + 1
 if F == 0:
  F = Y[0]
  S -=1
 print(int(F)*100 + S)