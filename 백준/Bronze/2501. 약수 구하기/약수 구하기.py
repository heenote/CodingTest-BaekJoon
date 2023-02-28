A = []
m , n= map(int,input().split())
for i in range(1,m+1):
    if m % i == 0:
       A.append(i)
if len(A) < n:
   print(0)
else:
   B = sorted(A)
   print(B[n-1])