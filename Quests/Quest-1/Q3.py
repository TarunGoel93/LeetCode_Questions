x = 1234
n = x
y = 0
while(x!=0):
  digit = x%10
  y=y*10+digit
  x = x//10

print(y)

if n<0:
  print("False")

if y==n:
  print("True")
else:
  print("False")