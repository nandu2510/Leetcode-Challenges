class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                if num[i]+num[j]==target:
                     return [i,j]
           