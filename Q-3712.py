nums = [1,2,2,3,3,3,3,4]
k = 2

count_map = {}
for i in nums:
  if i in count_map:
    count_map[i]+=1
  else:
    count_map[i]=1
print(count_map)

sum = 0
for key,value in count_map.items():
  if value%k==0:
    sum+=key*value

print(sum)