from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newest = []
        for num in nums:
            if num not in newest:
                newest.append(num)
        for i in range(len(newest)):
            nums[i]=newest[i]
        for k in range(len(newest),len(nums)):
            nums[k]="_"

        return len(newest)