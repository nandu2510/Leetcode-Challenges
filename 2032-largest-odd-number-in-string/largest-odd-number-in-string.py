class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):   # start from last index
            if int(num[i]) % 2 != 0:          # check if digit is odd
                return num[:i+1]              # return substring
        
        return ""                             # if no odd digit found
