from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        d=Counter(s)
        vow=set()
        cons=set()
        for char,freq in d.items():
            if char in "aeiou":
                vow.add(freq)
            else:
                cons.add(freq)
        maxv=max(vow) if vow else 0
        maxc=max(cons) if cons else 0
        return (maxc+maxv)
                
                
        