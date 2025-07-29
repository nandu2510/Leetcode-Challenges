class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        perm=0
        for i in set(s):
            perm+=abs(s.index(i)-t.index(i))
        return perm