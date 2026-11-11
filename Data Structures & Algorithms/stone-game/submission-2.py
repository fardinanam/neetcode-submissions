class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                dp[l][r] = max(dp[l + 1][r] + piles[l] \
                    , dp[l][r - 1] + piles[r])
        
        return dp[0][n - 1] > sum(piles) // 2