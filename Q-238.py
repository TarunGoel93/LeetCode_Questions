str = ["a","a","b","b","c","c","c"]

count_read = 0

for i in range(0,len(str),1):
  for j in range(i+1,len(str),1):
    if(str[i]==str[j]):
      count_read+=1
      



      