class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = sorted(nums, key = int)
        n = len(nums)
        middle = num[n // 2]
        return middle
                