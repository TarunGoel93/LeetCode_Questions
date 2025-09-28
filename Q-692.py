words = ["i","love","leetcode","i","love","coding"]
k = 2

count_map = {}
for i in words:
  if i in count_map:
    count_map[i]+=1
  else:
    count_map[i]=1

print(count_map)

x = []
for key,value in count_map.items():
  x.append((key,value))

x.sort(key=lambda item: item[1],reverse=True)
print(x)

y = []
for i in range(k):
    y.append(x[i][0])



print(sorted(y))




