class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        third_max=list(set(nums))
        if len(third_max)<3:
            return max(third_max)
        third_max.sort(reverse=True)
        return third_max[2]