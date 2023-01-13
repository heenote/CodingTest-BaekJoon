X = list(input().split(' '))
B = []
for i in X:
  if i == '':
    continue
  B.append(i)  
print(len(B))