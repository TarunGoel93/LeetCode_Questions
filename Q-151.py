s = "I am a boy"
words = []
word = ""
for i in range(0,len(s),1):
  if s[i]!=" ":
    word+=s[i]
  else:
    if word!="":
      words.append(word)
      word = ""
if word!="":
  words.append(word)

print(words)

x = []
for i in range(len(words)-1,-1,-1):
  x.append(words[i])
print(x)




# x = []
# start = len(s)
# for i in range(len(s)-1,-1,-1):
#   if s[i]==" ":
#     for j in range(i+1,start):
#       x.append(s[j])
#     x.append(" ")
#     start = i

# for j in range(0,start):
#   x.append(s[j])

# print("".join(x))


