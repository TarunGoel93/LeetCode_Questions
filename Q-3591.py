nums = [1,2,3,4,5]

count_map = {}
for i in nums:
  if i in count_map:
    count_map[i]+=1
  else:
    count_map[i]=1

print(count_map)

x = []
for key,value in count_map.items():
  x.append(value)

print(x)

for i in x:
  if i<2:
    continue
  prime = True
  for j in range(2,int(i**0.5)+1):
    if i%j==0:
      prime = False
      break
  if prime:
    print(True)
    break
else:
    print(False)