nums = [1,2,1,10]

x = sorted(nums)
print(x)

for i in range(len(x)-3,-1,-1):
  if x[i]+x[i+1]>x[i+2]:
    print(x[i]+x[i+1]+x[i+2])
print("0")

