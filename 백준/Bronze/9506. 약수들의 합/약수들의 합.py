B=[]
while True:
    X = int(input())
    if X == -1:
        break
    total = 0
    res = str(X) + " = "
    for i in range(1,X+1):
      if i == 1:
        res += str(i) 
        total += 1
      if X % i == 0 and X != i and i !=1:
        res += ' + ' + str(i)  
        total += i
    if total == X:
       B.append(res)
    elif total != X:
       B.append(str(X) + " is NOT perfect.")        
for j in range(len(B)):
   print(B[j])