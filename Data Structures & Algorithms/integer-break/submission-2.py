class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        elif n == 3:
            return 2

        dp = {}

        def dfs(m):
            if m in dp:
                return dp[m]
            
            if m <= 3:
                return m

            for i in range(1, m // 2 + 1):
                left = dfs(i)
                right = dfs(m - i)

                if m not in dp:
                    dp[m] = left * right
                else:
                    dp[m] = max(dp[m], left * right)

            return dp[m]
        
        return dfs(n)