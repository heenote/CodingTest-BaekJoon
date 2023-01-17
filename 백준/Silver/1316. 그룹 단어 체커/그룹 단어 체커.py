num = int(input())
cnt = 0
for _ in range(0,num):
  A = [0]
  X = input()
  for i in range(0, len(X)):
    if A[-1] == 0: 
     A.append(X[i])
    elif A[-1] == X[i]:
      continue
    elif A[-1] != X[i]:
      if X[i] not in A:
       A.append(X[i])
      else:
        num-=1
        break  
print(num)