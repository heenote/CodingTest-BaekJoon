X = int(input()) 
if X > 1:
    for i in range(2, X+1):
        if X % i == 0:
            while X % i ==0:
                print(i)
                X = X/i