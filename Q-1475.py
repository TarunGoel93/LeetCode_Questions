prices = [10,1,1,5]
x = []
for i in range(0,len(prices),1):
  discount = 0
  for j in range(i+1,len(prices),1):
    if prices[j]<=prices[i]:
      discount = prices[j]
      break
  x.append(prices[i]-discount)
print(x)