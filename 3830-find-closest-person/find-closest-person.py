import operator
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diffx=abs(operator.sub(x,z))
        diffy=abs(operator.sub(y,z))
        res=min(diffx,diffy)
        if res==diffx and res==diffy:
            return 0
        elif res==diffy:
            return 2
        return 1