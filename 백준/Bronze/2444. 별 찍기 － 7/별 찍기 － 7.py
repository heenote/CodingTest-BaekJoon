X = int(input())
for i in range(1, X+1):
    print(' ' * (X-i) + '*' * i + '*' * (i-1))
for j in range(X-1, 0,-1):
    print(' ' * (X-j) + '*' * j + '*' * (j-1))   