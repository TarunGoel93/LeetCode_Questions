n = 13

n_sq = n*n
n_cb = n*n*n

print(n_sq)
print(n_cb)

hex_part = format(n_sq,'X')

hexa_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
hexa_part = ''

num = n_cb
while(num>0):
  hexa_part = hexa_chars[num%36]+hexa_part
  num//=36



print(hexa_part)