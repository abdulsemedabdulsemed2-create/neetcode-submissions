class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max_pro:
                    max_pro =  prices[j] - prices[i]
                j += 1
            i += 1
        return max_pro