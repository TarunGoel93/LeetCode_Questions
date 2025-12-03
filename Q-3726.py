n = 1020030

x = []
while(n!=0):
  digit = n%10
  if digit!=0:
    x.append(digit)
  n = n//10
print(x)