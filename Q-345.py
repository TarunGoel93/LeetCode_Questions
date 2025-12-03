s = "IceCreAm"
reverse = []
for i in range(0,len(s),1):
  if(s[i] in ['a','e','i','o','u','A','E','I','O','U']):
    reverse.append(s[i])
print(reverse)

s_list = list(s)

k = len(reverse)-1
for i in range(0,len(s_list),1):
  if s_list[i] in ['a','e','i','o','u','A','E','I','O','U']:
    s_list[i] = reverse[k]
    k-=1

s = "".join(s_list)
print("Result:", s)




    

