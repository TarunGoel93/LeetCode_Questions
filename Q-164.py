nums = [3,6,9,1]
x = sorted(nums)
print(x)

max = 0
for i in range(0,len(x),1):
  diff = x[i]-x[i-1]
  if(diff>max):
    max = diff
  

print(max)