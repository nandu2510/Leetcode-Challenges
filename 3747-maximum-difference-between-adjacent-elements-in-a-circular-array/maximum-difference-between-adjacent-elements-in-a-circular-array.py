class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        # if len(nums)<2:
        #     return 0
        # nums.sort()
        # count = []
        # for i in range(len(nums) - 1):
        #     num = nums[i + 1] - nums[i]
        #     count.append(num)
        # return max(count)
        return max(abs(nums[i]-nums[i-1])for i in range(len(nums)))
