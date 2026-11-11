class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [grid[0][0]]

        for i in range(1, len(grid[0])):
            dp.append(dp[-1] + grid[0][i])

        for i in range(1, len(grid)):
            temp = [0] * len(grid[i])
            for j in range(len(grid[i])):
                temp[j] = grid[i][j] + dp[j]

                if j > 0 and temp[j] > grid[i][j] + temp[j - 1]:
                    temp[j] = grid[i][j] + temp[j - 1]
        
            dp = temp
        
        return dp[-1]
                    