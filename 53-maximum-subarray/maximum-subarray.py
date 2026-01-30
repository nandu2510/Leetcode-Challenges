class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        maxi = nums[0]
        n = len(nums)

        for i in range(1, n):
            sum += nums[i]

            if sum < nums[i]:
                sum = nums[i]

            if sum > maxi:
                maxi = sum

        return maxi
