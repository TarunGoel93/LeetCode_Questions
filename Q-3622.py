n = 23
orig_num = n
sum = 0
product = 1
while(n!=0):
  digit  = n%10
  sum = sum+digit
  product = product*digit
  n = n//10

if(orig_num%sum==0 and orig_num%product==0):
  print("True")
else:
  print("False")