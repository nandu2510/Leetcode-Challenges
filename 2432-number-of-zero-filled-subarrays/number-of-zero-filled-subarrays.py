
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        counter = 0
        total = 0
        for num in nums:
            if num == 0:
                counter += 1
                total += counter
            else:
                counter = 0
        return total