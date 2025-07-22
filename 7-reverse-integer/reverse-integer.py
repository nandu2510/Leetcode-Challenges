class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Step 1: Handle sign
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Step 2: Reverse the number
        reversed_num = 0
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10

        # Step 3: Add sign back
        reversed_num = reversed_num * sign

        # Step 4: Check range
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num