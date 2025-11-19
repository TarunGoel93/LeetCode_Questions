arr = ["a","b","a"]
k = 3

count_map = {}
for i in arr:
  if i in count_map:
    count_map[i]+=1
  else:
    count_map[i]=1


x = []
for key,value in count_map.items():
  if value==1:
    x.append(key)

if 1<=k<=len(x):
  print(x[k-1])
else:
  print("srt")
