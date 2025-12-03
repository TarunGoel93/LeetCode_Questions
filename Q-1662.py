word1 = ["ab","c"]
word2 = ["a","bc"]

w1 = ""
w2 = ""

for i in word1:
  w1+=i

for i in word2:
  w2+=i

if(w1==w2):
  print(True)
else:
  print(False)
