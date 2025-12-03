n = 17

a = []
for i in range(1,n+1,1):
  num = i
  bits = ""
  while(num>0):
    bits = str(num%2)+bits
    num = num//2
  a.append(bits)
print(a)

total_bits = 0
for i in a:
  for j in i:
    if j=='1':
      total_bits+=1
print(total_bits)