num = "1234"

nums = ""
num_arr = []

for i in num:
  if i !=" ":
    nums=i
    num_arr.append(int(nums))

print(num_arr)

odd_sum = 0
even_sum = 0

for i in range(0,len(num_arr),1):
  if(i%2!=0):
    odd_sum+=num_arr[i]
  elif(i%2==0):
    even_sum+=num_arr[i]

print(odd_sum)
print(even_sum)

if(odd_sum==even_sum):
  print(True)
else:
  print(False)
