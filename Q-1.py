import math

paragraph = "a, a, a, a, b,b,b,c, c"
banned = "a"

x = paragraph.lower()
y = banned.lower()
z = ""

for i in x:
  if(i!=',' and i!='.'):
    z += i


word = ""
words = []

for i in z:
  if i!=" ":
    word+=i
  else:
    if word:
      words.append(word)
      word = ""
if word:
    words.append(word)

filter_words = []

for i in words:
  if i!=y:
    filter_words.append(i)



count_map = {}

for i in filter_words:
  if i in count_map:
    count_map[i]+=1
  else:
    count_map[i]=1
print(count_map)

a = -1
b = ""
for key,value in count_map.items():
  a = max(a,value)
  if a == value:
    b = key

print(a)
print(b)
