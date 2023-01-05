A= []
result =[]
for i in range(10):
    X = int(input())
    B = X % 42
    A.append(B)
    
for value in A:
    if value not in result:    
      result.append(value)


print((len(result)))