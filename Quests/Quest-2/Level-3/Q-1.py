s = "abbaca"

x = []

for i in range(0,len(s),1):
  if s[i]==x[-1] and i>0:
 
    x.pop()
  else:
    x.append(s[i])

print("".join(x))