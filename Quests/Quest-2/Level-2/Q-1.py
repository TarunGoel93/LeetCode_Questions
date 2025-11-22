nums = [1,1]

count_map = {}
for i in nums:
  if i in count_map:
    count_map[i]+=1
  else:
    count_map[i]=1

x = []
for key,value in count_map.items():
  if value==2:
    x.append(key)

s = set(nums)
for i in range(1,len(nums)+1,1):
  if i not in s:
    x.append(i)

print(x)