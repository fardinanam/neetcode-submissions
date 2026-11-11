class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2
        n = len(stones)
        
        dp = [[0] * (target + 1) for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]

                if stones[i - 1] <= j:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1])
        
        return abs(stoneSum - 2 * dp[n][target])
