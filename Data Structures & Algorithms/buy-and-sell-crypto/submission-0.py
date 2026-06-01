class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = prices[0], 0

        for i in prices:
            if i < minPrice:
                minPrice = i

            else: 
                profit = i - minPrice

                maxProfit = max(maxProfit, profit)

        return maxProfit