class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}

        def dfs(n):
            if n == 0:
                return 0

            if n in dp:
                return dp[n]
            
            high = math.floor(math.sqrt(n))

            dp[n] = n
    
            for i in range(high, 0, -1):
                square = i ** 2
                if square > n:
                    continue
                
                dp[n] = min(dp[n], 1 + dfs(n - square))

            return dp[n]
        
        return dfs(n)
