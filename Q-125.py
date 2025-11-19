s = "A man, a plan, a canal: Panama"

x = s.lower()
print(x)

y = []
for i in range(0,len(x),1):
  if 'a'<=x[i]<='z':
    y.append(x[i])

print(y)


a = []
flag = True
for i in range(len(y)):
  if y[i]!=y[-(i+1)]:
    flag = False
    break
  

print(flag)



# s = 'abba'
# flag = True
# for i in range(0,len(s),1):
#   if s[i]!=s[-(i+1)]:
#     flag = False



# s = 'Geeks'
# x = []
# for i in range(len(s)-1,-1,-1):
#   x.append(s[i])
# print("".join(x))