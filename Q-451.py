s = "tree"
x = []
for i in range(len(s)):
  x.append(s[i])

count_map = {}

for i in x:
  if i in count_map:
    count_map[i]+=1
  else:
    count_map[i]=1

print(count_map)

a = []
for key,value in count_map.items():
  a.append((key,value))

print(a)

a.sort(key=lambda item: item[1],reverse=True)

print(a)

b = []
for i in range(len(a)):
  for j in range(a[i][1]):
    b.append(a[i][0])

print(b)

c = ""
for i in b:
  c+=i
print(c)