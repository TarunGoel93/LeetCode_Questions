a = 12
b = 6

x = []
y = []
z = []

for i in range(1,a+1,1):
  if(a%i==0):
    x.append(i)

for i in range(1,b+1,1):
  if(b%i==0):
    y.append(i)

for i in x:
  for j in y:
    if i==j:
      z.append(i)

print(x)
print(y)
print(z)
