s = "42"

stack = []

for i in s:
  if i.isdigit():
    stack.append(int(i))
  elif i=="+" or i=='-' or i=='*' or i=='/':
    stack.append(i)
  # else:
  #   stack.append(i)
print(stack)

i = 0
while i<len(stack):
  if stack[i]=='*':
    current_answer = stack[i-1]*stack[i+1]
    stack[i-1:i+2] = [current_answer]
    i-=1
  elif stack[i]=='/':
    current_answer = stack[i-1]//stack[i+1]
    stack[i-1:i+2] = [current_answer]
    i-=1
  else:
    i+=1
print(stack)  

result = stack[0]
for i in range(1,len(stack),2):
  if stack[i]=='+':
    result+=stack[i+1]
  elif stack[i]=='-':
    result-=stack[i+1]

print(result)