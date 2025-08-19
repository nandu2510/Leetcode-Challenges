class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            num=sum(int(str(num)[i]) for i in range(len(str(num))))
        return num