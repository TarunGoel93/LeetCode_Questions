nums = [10,12,19,14]
original = nums[:]

seen = {}
max_sum = -1
for i in range(0,len(nums),1):
  sum = 0
  n = nums[i]
  while(n!=0):
    digit = n%10
    sum+=digit
    n//=10

  if sum in seen:
    max_sum = max(max_sum,seen[sum]+original[i])
    seen[sum] = max(seen[sum],original[i])
  else:
    seen[sum] = original[i]

print(max_sum)


