class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_zero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[last_zero],nums[i]=nums[i],nums[last_zero]
                last_zero+=1
        