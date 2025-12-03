sentence = "leet"

flag = True
for i in range(ord('a'),ord('z'),1):
  if chr(i) not in sentence:
    flag = False
    break

print(flag)
