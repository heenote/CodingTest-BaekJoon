X = int(input())
Y = map(int,(input().split()))            
cnt = 0  
for i in Y:
    check = 0
    if i >1:
        for j in range(2, i):
            if i % j == 0:
              check += 1
        if check == 0:
            cnt+=1    
print(cnt)   