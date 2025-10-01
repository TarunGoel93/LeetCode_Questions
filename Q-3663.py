n = 723344511

x = []
while(n!=0):
  digit = n%10
  x.append(digit)
  n = n//10
print(x)

count_map = {}
for i in x:
  if i in count_map:
    count_map[i]+=1
  else:
    count_map[i]=1
print(count_map)

min_value = -1
for value in count_map.values():
  if min_value==-1 or value<min_value:
    min_value = value



min_key = -1
for key,value in count_map.items():
  if value==min_value:
    if min_key==-1 or key<min_key:
      min_key = key
print(min_key)