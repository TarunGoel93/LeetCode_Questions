s = "abccbaacz"

x = ""
for i in range(0,len(s),1):
  if s[i]==s[i+1]:
    x = s[i]
    break

print(x)
