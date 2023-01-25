ary = ['c=','c-','dz=','lj','d-','nj','s=','z=']
X = input()
A = []
for i in ary:
 X = X.replace(i,'@') 
print(len(X))  