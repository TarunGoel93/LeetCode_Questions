n = 267

x = []

while(n!=0):
  digit = n%10
  x.append((digit))
  n = n//10

max_nums = sorted(x)

print(max_nums)

result = max_nums[-1]*max_nums[-2]

print(result)