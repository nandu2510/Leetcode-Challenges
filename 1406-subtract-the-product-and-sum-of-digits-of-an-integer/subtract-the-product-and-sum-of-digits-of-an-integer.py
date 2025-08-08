class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product,adition=1,0
        for i in str(n):
            ch=int(i)
            product*=ch
            adition+=ch
        return product-adition
         
