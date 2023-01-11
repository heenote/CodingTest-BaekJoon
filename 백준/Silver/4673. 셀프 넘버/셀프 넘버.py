b = set(range(1, 10001))
ary = set()
for i in b:
  for j in str(i):
    i += int(j)
  ary.add(i)

num = sorted(b - ary) 
for s in num:
 print(s)