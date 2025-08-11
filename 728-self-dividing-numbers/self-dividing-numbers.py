class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isDivide(n):
            nums=n
            while n>0:
                rem=n%10
                if rem==0:
                    return False
                if nums%rem!=0:
                    return False
                n//=10
            return True
        res=[]
        for i in range(left,right+1):
            if isDivide(i):
                res.append(i)
        return res