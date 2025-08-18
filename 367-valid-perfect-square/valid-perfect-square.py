# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         for i in range(1,32):
#             if pow(i,2)==num:
#                 return True
#         return False
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i <= num:
            if i * i == num:
                return True
            i += 1
        return False
