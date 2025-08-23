# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         seen=set(s)
#         return len(seen)
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res,n=0,len(s)
        dd=defaultdict(int)
        l=0
        for r in range(n):
            dd[s[r]]+=1
            while dd[s[r]]>1:
                dd[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res