nums = [2,2]

max = len(nums)
min = 1
s = set(nums)
x = []
for i in range(min,max+1,1):
  if i not in s:
    x.append(i)
print(x)