class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        stack=[]
        for i in range(len(hours)):
            if hours[i]>=target:
                stack.append(hours[i])
        return len(stack)