s = "leetcode"

count_map = {}

for i in s:
  if i in count_map:
    count_map[i]+=1
  else:
    count_map[i] = 1
print(count_map)

x = ""
for key,value in count_map.items():
  if value == 1:
    x = key
    break
print(x)