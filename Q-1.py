<<<<<<< HEAD
n = 17

a = []
for i in range(1,n+1,1):
  num = i
  bits = ""
  while(num>0):
    bits = str(num%2)+bits
    num = num//2
  a.append(bits)
print(a)

total_bits = 0
for i in a:
  for j in i:
    if j=='1':
      total_bits+=1
print(total_bits)
=======
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
>>>>>>> 29e8dd0ceb10b203bf890dcb5e35c1779093d59a
