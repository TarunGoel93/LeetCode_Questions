nums = [2,3,5,1,3]
n = 3

pre_ans = []

for i in range(0,len(nums),1):
  pre_ans.append(nums[i]+n)

print(pre_ans)

final_ans = []

maxi_cand = max(nums)

for i in range(0,len(nums),1):
  if(pre_ans[i]>=maxi_cand):
    final_ans.append("True")
  else:
    final_ans.append("False")

print(final_ans)
  