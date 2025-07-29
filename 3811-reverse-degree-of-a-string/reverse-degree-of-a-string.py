class Solution:
    def reverseDegree(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            ele=26+ord("a")-ord(s[i])
            count+=ele*(i+1)
        return count