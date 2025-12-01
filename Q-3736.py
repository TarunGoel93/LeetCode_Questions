nums = [2,1,3]

max = nums[0]
for i in range(0,len(nums),1):
  if max<nums[i]:
    max = nums[i]
print(max)

count = 0
for i in range(0,len(nums),1):
  count+=max-nums[i]
print(count)