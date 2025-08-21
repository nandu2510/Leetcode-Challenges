from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k = 0  # pointer for the next position to keep
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k] = nums[i]
        #         k += 1
        # return k
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
