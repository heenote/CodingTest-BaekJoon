n, m = map(int, input().split())
farr = list(list(map(int,input().split()))for _ in range(n))
sarr = list(list(map(int,input().split()))for _ in range(n))
for x in range(n):
    for y in range(m):
        print(farr[x][y] + sarr[x][y], end=' ')
    print() 