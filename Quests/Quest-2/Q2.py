class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(0,n,1):
            result.append(nums[i])
            result.append(nums[i+n])
        return result