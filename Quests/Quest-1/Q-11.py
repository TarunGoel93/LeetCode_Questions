n = 8
x = []
for i in range(2,n+1,1):
  if n%i==0:
    x.append(i)
print(x)
mul = 1
y = []
for i in range(0,len(x),1):
  if x[i] not in [2,3,5]:
    break
  mul*=x[i]
  y.append(x[i])
  if mul==n: 
    break 
print(mul)
print(y)
flag = True
for i in range(0,len(y),1):
  if y[i] not in [2,3,5]:
    flag = False
if mul != n:
    flag = False
print(flag)