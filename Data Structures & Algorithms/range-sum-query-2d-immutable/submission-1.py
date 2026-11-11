class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.cumSumMat = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            rowCumSum = 0
            for j in range(len(matrix[i])):
                rowCumSum += matrix[i][j]
                self.cumSumMat[i][j] = rowCumSum

                if i > 0:
                    self.cumSumMat[i][j] = self.cumSumMat[i - 1][j] + rowCumSum

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.cumSumMat[row2][col2]

        if row1 > 0:
            res -= self.cumSumMat[row1 - 1][col2]
        
        if col1 > 0:
            res -= self.cumSumMat[row2][col1 - 1]
        
        if row1 > 0 and col1 > 0:
            res += self.cumSumMat[row1 - 1][col1 - 1]

        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)