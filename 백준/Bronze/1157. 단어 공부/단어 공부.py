X = list(input().upper())
A = list(set(X))
B= []
for j in A:
  cnt = X.count(j)
  B.append(cnt)
if B.count(max(B)) > 1:
  print('?')
else:
  print(A[B.index(max(B))]) 