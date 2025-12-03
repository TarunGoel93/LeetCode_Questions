num = 8

num1 = num+1
num2 = num+2

x = []
for i in range(2,num2+1,1):
  for j in range(i,num2+1,1):
    if i*j==num2:
      x.append([i,j])

y = []
for i in range(2,num1+1,1):
  for j in range(i,num1+1,1):
    if i*j==num1:
      y.append([i,j])
  
    
print(y)

sub1 = 0
for i in y:
  sub1 = abs(i[0]-i[1])
print(sub1)

sub2 = 0
for i in x:
  sub2 = abs(i[0]-i[1])
print(sub2)

if sub2>sub1:
  print(y)
else:
  print(x)