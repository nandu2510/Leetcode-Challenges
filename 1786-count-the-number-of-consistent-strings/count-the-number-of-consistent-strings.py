class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=set(allowed)
        count=0
        for i in words:
            if set(i).issubset(allowed):
                count+=1
        return count