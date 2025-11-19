heights = [1,2,3,4,5]

s = sorted(heights)


count = 0
for i in range(0,len(s),1):

    if s[i]!=heights[i]:
      count+=1

print(count)