X = int(input())
n = 0
last = 1
if X == 1:
  print(1)  
while X > 1:  
 if X > last:
  n+=1
  last += 6*n
 elif X <= last:
  print(n+1)
  break