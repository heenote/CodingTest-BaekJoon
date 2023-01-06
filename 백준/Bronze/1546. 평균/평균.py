A = []
X = int(input())
Y = (input().split())
for i in range(X):
  if i == 0:  
   A.append(int(Y[i]))
  else:
    if A[i-1] > int(Y[i]):
        A.insert(0,int(Y[i])) 
    else:
         A.append(int(Y[i]))   

for j in range(len(A)):
    A[j] = round((A[j] / A[-1] * 100), 2)

print( f'{(sum(A) / X) : .2f}' )