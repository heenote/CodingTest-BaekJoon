ary =[]
ary2 =[]
for _ in range(3):
 m, n = map(int,input().split())
 ary.append(m)
 ary2.append(n)
for i in range(3):
 if ary.count(ary[i]) == 1:
  x = ary[i]
 if ary2.count(ary2[i]) == 1:
  y = ary2[i] 
print(x,y)