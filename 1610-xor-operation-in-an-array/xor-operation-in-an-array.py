class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        val=start
        # n=len(nums)
        for i in range(1,n):
            val^=(start + 2 * i)
        return val