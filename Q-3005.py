nums = [1,2,2,3,3,1,4]

count_map = {}
for i in nums:
  if i in count_map:
    count_map[i]+=1
  else:
    count_map[i]=1
print(count_map)

x = max(count_map.values())
y = []
sum = 0
for key,value in count_map.items():
  if value == x:
    y.append(value)

print(y)

for i in y:
  sum+=i

print(sum)