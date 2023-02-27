farr = list(list(input())for _ in range(5))
max_length = 0    
res =''  
for i in farr:
 if max_length < len(i):
  max_length = len(i) 
for j in range(max_length):
     for k in range(5):
      if j < len(farr[k]):
       res += farr[k][j]
print(res) 