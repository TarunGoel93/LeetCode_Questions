nums = [1,0,1,1,1,0,1]
max_count = 0
count = 0
for i in range(0,len(nums),1):
  if nums[i]==1:
    count+=1
    if count>max_count:
      max_count = count
  else:
    count = 0
print(max_count)

