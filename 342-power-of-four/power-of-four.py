class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(32):
            if n==pow(4,i):
                return True
            
        return False