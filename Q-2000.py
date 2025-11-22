word = "abcdefd"
ch = "d"

x = []
index = -1
for i in range(0,len(word),1):
  if ch == word[i]:
    index = i
    break
x = []
for i in range(index,-1,-1):
  x.append(word[i])
print(x)

for i in range(index+1,len(word),1):
  x.append(word[i])
print(x)