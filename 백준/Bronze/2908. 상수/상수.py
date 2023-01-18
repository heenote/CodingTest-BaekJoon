A = []
X = input().split()
for i in X:
  res =""
  for j in reversed(i):
    res = res + j
  A.append(res)
print(A[0] if int(A[0]) > int(A[1]) else A[1]) 