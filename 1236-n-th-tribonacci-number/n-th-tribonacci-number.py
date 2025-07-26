class Solution:
    def tribonacci(self, n: int) -> int:
        res={}
        def fib(n):
            if n==0:
                return 0
            if n<=2:
                return 1
            if n not in res:
                res[n]=fib(n-1)+fib(n-2)+fib(n-3)
            return res[n]
        return fib(n)