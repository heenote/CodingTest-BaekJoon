A = [1, 1, 2, 2, 2, 8]
X = input().split()

for i in range(0, len(A)):
    print(int(A[i]) - int(X[i]), end =' ')
