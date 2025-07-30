class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Go from the end toward the start
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0  # carry over

        # If all digits were 9, we need to add 1 at the beginning
        return [1] + digits
