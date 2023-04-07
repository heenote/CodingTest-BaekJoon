X= int(input())
ary =[]
ary2=[]
if X == 1:
    print(0)
else:     
 for _ in range(X):
    m, n = map(int,input().split())    
    ary.append(m)
    ary2.append(n)
 a = max(ary) - min(ary)
 b = max(ary2) - min(ary2)
 print(a*b)  