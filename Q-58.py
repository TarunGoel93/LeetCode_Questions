str1 = "   fly me   to   the moon  "
count = 0

for i in range(len(str1)-1,-1,-1):
  if(str1[i]==" "):
    if count>0:
      break
  else:
    count+=1


print(count)