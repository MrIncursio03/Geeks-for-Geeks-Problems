class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        res = 0
        for i in range (1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
