import math

left = 10
right = 19

x = []

for i in range(left,right+1,1):
  if i <2:
     continue
  prime = True
  for j in range(2,int(i**0.5)+1,1):
    if i%j == 0:
      prime = False
      break
  if prime:
      x.append(i)

print(x)

y = []
min_diff = math.inf

for i in range(len(x)):
   for j in range(i+1,len(x),1):
      diff = abs(x[i]-x[j])
      if diff<min_diff:
         min_diff = diff
         y = [[x[i],x[j]]]
      elif diff == min_diff:
         y.append([x[i],x[j]])

print(y)

if y:
  min_pair = y[0]
  for i in y:
    if(min(i)<min(min_pair)):
        min_pair = i

  if(min_pair):
    print(min_pair)
else:
    print("-1")


         




