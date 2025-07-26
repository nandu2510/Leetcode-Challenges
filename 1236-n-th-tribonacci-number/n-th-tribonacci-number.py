class Solution:
    def tribonacci(self, n: int) -> int:
        res={}
        def fib(n,res):
            if n==0:
                return 0
            if n<=2:
                return 1
            if n not in res:
                res[n]=fib(n-1,res)+fib(n-2,res)+fib(n-3,res)
            return res[n]
        return fib(n,res)