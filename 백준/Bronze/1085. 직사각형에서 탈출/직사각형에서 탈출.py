x, y, w, h = map(int,input().split())
ary = []
ary.append(w-x)
ary.append(h-y)
ary.append(x)
ary.append(y)
print(min(ary))