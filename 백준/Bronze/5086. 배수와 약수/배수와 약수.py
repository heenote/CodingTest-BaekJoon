A = []
while True:
 m , n= map(int,input().split())
 if m == 0 and n == 0:
  break
 if m < n and n % m == 0:
  A.append('factor')
 elif m > n and m % n == 0:
  A.append("multiple")
 else: A.append('neither')  
for i in A:
 print(i, sep='\n')