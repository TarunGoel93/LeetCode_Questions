tokens = ["2","1","+","3","*"]

x = []

for i in tokens:

  if i in ['+','-','*','/']:
    b = x.pop()
    a = x.pop()

  
    if i=='+':
      x.append(a+b)
    elif i == '-':
      x.append(a-b)
    elif i == '*':
      x.append(a*b)
    elif i=='/':
      x.append(a/b)
  else:
    x.append(int(i))

print(x)