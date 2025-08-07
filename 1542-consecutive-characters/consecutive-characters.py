class Solution:
    def maxPower(self, s: str) -> int:
        count,answer=1,1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
                answer=max(count,answer)
            else:
                count=1
        return answer
