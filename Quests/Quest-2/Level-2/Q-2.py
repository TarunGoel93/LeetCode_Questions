nums = [8,1,2,2,3]


x = []
for i in range(0,len(nums),1):
  count = 0
  for j in range(0,len(nums),1):
    if nums[i]>nums[j] and j!=i:
      count+=1
  x.append(count)
print(x)