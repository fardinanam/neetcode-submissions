class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        dp = dict()

        def dfs(i, total):
            if (i, total) in dp:
                return dp[(i, total)]
    
            if total >= stoneSum / 2 or i == len(stones):
                dp[(i, total)] = abs(stoneSum - 2 * total) 
            else:
                dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
    
            return dp[(i, total)]

        return dfs(0, 0)
