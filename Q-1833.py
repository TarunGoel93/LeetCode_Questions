costs = [10,6,8,7,7,8]
coins = 5

count = 0
sum = 0
for i in range(0,len(costs),1):
  if sum+costs[i]<=coins:
    sum+=costs[i]
    count+=1
print(count)
