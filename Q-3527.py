message = ["s","a","aj","ps","h","ou","e","i","x"]
bannedWords = ["j","a","b","fa","z","a","no","ih","nq"]

count = 0
for i in message:
  for j in bannedWords:
    if(i==j):
      count+=1
      break
if count>=2:
  print("True")
else:
  print("False")    

