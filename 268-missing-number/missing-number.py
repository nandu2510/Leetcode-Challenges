class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result=list(range(0,len(nums)+1))
        return sum(result)-sum(nums)