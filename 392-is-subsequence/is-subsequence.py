class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k=0
        for i in range(len(t)):
            if k<len(s) and s[k]==t[i]:
                k+=1
        return k==len(s)