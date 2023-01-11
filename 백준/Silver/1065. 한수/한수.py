def solve(num):
  cnt = 0
  if num < 100:
    print(num)
  else:
    for i in range(100, num+1):
      s = []
      for j in str(i):
          s.append(int(j))
      if s[2] -s[1] == s[1] - s[0]:
       cnt+=1
    print(99+cnt)    
num = int(input())
solve(num)