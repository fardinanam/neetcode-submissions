class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1]

        for i in range(1, target + 1):
            dp.append(0)

            for num in nums:
                if i < num:
                    continue
                
                dp[-1] += dp[i - num]
        
        return dp[-1]