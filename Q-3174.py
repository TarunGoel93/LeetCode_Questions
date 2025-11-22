s = "cb"
x = []
count = 0
for i in s:
  if i in ['0','1','2','3','4','5','6','7','8','9']:
    if x:
      x.pop()
  else:
    x.append(i)

print("".join(x))

