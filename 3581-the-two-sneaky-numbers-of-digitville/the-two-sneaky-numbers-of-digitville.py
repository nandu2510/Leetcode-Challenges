class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        seen=set()
        for i in nums:
            if i in seen:
                res.append(i)
            else:
                seen.add(i)
        return res