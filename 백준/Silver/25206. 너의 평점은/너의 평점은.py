grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0':3.0, 'C+': 2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0,'P':0}
sum = 0
athSum = 0
arr = list((input().split()) for _ in range(20))
for i in arr:
    if i[2] != 'P':
      athSum += float(i[1])
    sum+= float(i[1]) * grade[i[2]]
print(round((sum/athSum),6))