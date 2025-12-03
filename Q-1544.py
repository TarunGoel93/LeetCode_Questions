ops = ["1","C"]

x = []

for i in range(0,len(ops),1):
  if ops[i].lstrip('-').isdigit():
    x.append(int(ops[i]))
  elif ops[i]=='C':
    x.pop()
  elif ops[i]=='D':
    x.append(2*x[-1])
  elif ops[i]=='+':
    x.append((x[-1])+(x[-2]))
print(sum(x))