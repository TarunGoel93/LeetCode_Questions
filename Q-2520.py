n = 1248
org = n

x = []
while(n!=0):
  digit = n%10
  x.append(digit)
  n = n//10

print(x)

count = 0
for i in range(0,len(x),1):
  if(org%x[i]==0):
    count+=1

print(count)
