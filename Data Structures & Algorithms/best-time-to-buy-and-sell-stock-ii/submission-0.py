class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smaller = larger = 0

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] <= prices[larger]:
                profit += prices[larger] - prices[smaller]
                smaller = larger = i
            else:
                larger = i

        return profit + prices[larger] - prices[smaller]