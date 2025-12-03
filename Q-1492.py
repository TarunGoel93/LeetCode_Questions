n = 4
k = 4

count = 0
x = -1

for i in range(1,n+1,1):
  if(n%i==0):
    count+=1
    if count==k:
      x = i
      break

print(x)