temperatures  = [73,74,75,71,69,72,76,73]

x = []

for i in range(0,len(temperatures),1):
  count = 0
  for j in range(i+1,len(temperatures),1):
    count+=1
    if temperatures[i]<temperatures[j]:
      x.append(count)
      break
  else:
    x.append(0)
    
print(x)
