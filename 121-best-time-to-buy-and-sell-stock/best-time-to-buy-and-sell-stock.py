class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxprofit=0
        n=len(prices)
        for i in range(n):
            cost=prices[i]-mini
            maxprofit=max(maxprofit,cost)
            mini=min(mini,prices[i])
        return maxprofit