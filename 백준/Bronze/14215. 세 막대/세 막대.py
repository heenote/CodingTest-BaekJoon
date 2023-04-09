X = sorted(map(int,input().split()))
res = X[0] + X[1] + min(X[2], X[0] + X[1] -1)
print(res)