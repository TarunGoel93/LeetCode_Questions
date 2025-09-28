x = 2.10000
n = 3

mul = 1.0

if(n<0):
  for i in range(1,abs(n)+1,1):
    mul*=x
  result = 1/mul
  print(result)
else:
  for i in range(1,n+1,1):
    mul*=x
  print(mul)

  
