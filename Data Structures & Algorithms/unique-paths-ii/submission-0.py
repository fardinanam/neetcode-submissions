class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [0] * len(obstacleGrid[0])

        dp[0] = 1 - obstacleGrid[0][0]

        for i in range(1, len(obstacleGrid[0])):
            if dp[i - 1] == 0 or obstacleGrid[0][i] == 1:
                break
            dp[i] = 1
        
        for i in range(1, len(obstacleGrid)):
            temp = [0] * len(obstacleGrid[i])
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 0:
                    temp[j] = dp[j]

                    if j > 0:
                        temp[j] += temp[j - 1]

            dp = temp

        return dp[-1]