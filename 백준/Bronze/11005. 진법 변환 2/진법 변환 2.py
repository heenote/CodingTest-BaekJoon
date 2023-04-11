m,n = map(int, input().split())
base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ''
while m > 0:
  res += base[m % n]
  m = m // n
print(res[::-1]) 