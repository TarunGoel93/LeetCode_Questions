s = "rat"
t = "car"

a = sorted(s)
b = sorted(t)

flag = True
for i in range(len(a)):
  if a[i]!=b[i]:
    flag = False
    break
print(flag)

