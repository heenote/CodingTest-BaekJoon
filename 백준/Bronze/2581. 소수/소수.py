import math
X = int(input())
Y = int(input())
cnt =[]
for i in range(X,Y+1):
    check = 0
    if i >1:
        for j in range(2, int(math.sqrt(i)+1)):
            if i % j == 0:
              check += 1
        if check == 0:
            cnt.append(i)    
if len(cnt) == 0:
   print(-1)
else:
   print(sum(cnt))    
   print(cnt[0])     