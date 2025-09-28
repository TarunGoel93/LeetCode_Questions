text = "hello world"
brokenLetters = "ad"

x = []
y = []
word = ""
word1 = ""
for i in text:
  if i != " ":
    word+=i
  else:
    x.append(word)
    word = ""
if word:
  x.append(word)
print(x)

for i in brokenLetters:
  if i != " ":
    word1+=i
  else:
    y.append(word1)
    word1 = ""
if word:
  y.append(word1)
print(y)