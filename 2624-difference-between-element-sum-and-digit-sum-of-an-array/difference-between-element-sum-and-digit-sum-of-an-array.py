class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        numsSum=sum(nums)
        eleSum=0
        for i in nums:
            for d in str(i):
                eleSum+=int(d)
        return abs(numsSum-eleSum)
            