nums = [-100, -98, -1, 2, 3, 4]

x = []
for i in range(len(nums)):
    x.append((nums[i]))

print(x)

y = sorted(x)
print(y)

# for i in range(len(y)-1,-1,-1):
#     print(y[i])

mul = max(y[-1]*y[-2]*y[-3], y[0]*y[1]*y[-1])

print(mul)
