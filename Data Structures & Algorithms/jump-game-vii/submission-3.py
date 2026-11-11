class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * len(s)
        dp[0] = True

        reachable = 0

        for i in range(1, len(s)):
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                reachable -= 1
            
            if i - minJump >= 0 and dp[i - minJump]:
                reachable += 1
            
            if reachable > 0 and s[i] == '0':
                dp[i] = True
        
        return dp[len(s) - 1]