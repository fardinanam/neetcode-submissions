class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]

        for i in range(2, n + 1):
            high = math.floor(math.sqrt(i))

            for j in range(1, high + 1):
                dp[i] = min(dp[i], 1 + dp[i - j ** 2])
        
        return dp[-1]
