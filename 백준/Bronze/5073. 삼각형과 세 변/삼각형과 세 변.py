while True:
    ary = []
    a,b,c = map(int, input().split())
    ary.append(a)
    ary.append(b)
    ary.append(c)
    if a == 0 and b == 0 and c == 0:
        break
    if len(set(ary)) == 1 :
        print('Equilateral')
    elif max(ary) >= sum(ary) - max(ary):
         print('Invalid') 
    elif len(set(ary)) == 3:
         print('Scalene')
    elif len(set(ary)) == 2:
        print('Isosceles')