class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
      def removechar(s):
        stack=[]
        for i in s:
            if i=="#" and stack:
                stack.pop()
            if i!="#":
                stack.append(i)
        return stack
      return removechar(s)==removechar(t)