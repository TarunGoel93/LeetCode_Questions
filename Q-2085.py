words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]

count_map1 = {}
for i in words1:
  if i in count_map1:
    count_map1[i]+=1
  else:
    count_map1[i]=1

count_map2 = {}
for i in words2:
  if i in count_map2:
    count_map2[i]+=1
  else:
    count_map2[i]=1

print(count_map1)
print(count_map2)

count = 0
for key1,value1 in count_map1.items():
  for key2,value2 in count_map2.items():
    if key1==key2 and value1==1 and value2==1:
        count+=1

print(count)

    