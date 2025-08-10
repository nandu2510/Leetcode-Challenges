class Solution:
    def minElement(self, nums: List[int]) -> int:
        count=[]
        for i in range(len(nums)):
            digit_sum = sum(int(d) for d in str(nums[i]))
            count.append(digit_sum)
        return min(count)