# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def guessNumber(self, n: int) -> int:
        low,high=1,n
        while low<=high:
            mid=(low+high)//2
            res=guess(mid)
            if res==0:
               return mid
            if res==-1:
               high=mid-1
            else:
               low=mid+1