nums = [8,4]

min = nums[0]
for i in range(0,len(nums),1):
  if min>nums[i]:
    min = nums[i]
# print(min)

max = nums[0]
for i in range(0,len(nums),1):
  if max<nums[i]:
    max = nums[i]
# print(max)

r = []
for i in range(min,max+1,1):
  if i not in nums:
    r.append(i)

print(r)