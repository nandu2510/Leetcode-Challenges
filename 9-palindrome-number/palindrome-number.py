class Solution:
    def isPalindrome(self, x: int) -> bool:
        # str_x = str(x)
        # return str_x == str_x[::-1]
        if x < 0:
            return False  # Negative numbers are not palindromes

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num

