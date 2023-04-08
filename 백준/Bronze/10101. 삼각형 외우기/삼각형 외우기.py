ary=[]
for _ in range(3):
    X=int(input())
    ary.append(X)
if ary.count(60) == 3:
    print('Equilateral')
elif sum(ary) == 180 and len(set(ary)) == 2:
    print('Isosceles')
elif sum(ary) == 180 and len(set(ary)) == 3:
    print('Scalene')
elif sum(ary) != 180:
    print('Error')   