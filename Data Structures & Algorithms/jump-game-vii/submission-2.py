class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * len(s)
        dp[0] = True

        for i in range(1, len(s)):
            if s[i] == '1':
                continue

            for j in range(max(0, i - maxJump), i - minJump + 1):
                dp[i] = dp[i] or dp[j]

                if dp[i] == True:
                    break
        
        return dp[len(s) - 1]