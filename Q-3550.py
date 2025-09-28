nums = [1,10,11]



for i in range(0,len(nums),1):
  sum = 0
  j = nums[i]
  while(j!=0):
      digit = j%10
      sum = sum+digit
      j = j//10
    

  if (sum == i):
    print(i)
    break
else:
  print("-1")