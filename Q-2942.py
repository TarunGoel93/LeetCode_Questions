words = ["leet","code"]
x = "e"

y = []
for i in range(0,len(words),1):
  if x in words[i]:
    y.append(i)
print(y)
