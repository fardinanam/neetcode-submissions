class Solution:
    def candy(self, ratings: List[int]) -> int:
        def calcDesc(i, lastMax):
            j = i + 1
            while j < len(ratings) and ratings[j] < ratings[j - 1]:
                j += 1
            
            n = j - i
            cnt = (n * (n + 1)) // 2

            if lastMax <= n:
                cnt += n - lastMax + 1
            
            return cnt, j
        
        totalCnt = 1
        lastCnt = 1
        i = 1

        while i < len(ratings):
            if ratings[i] > ratings[i - 1]:
                lastCnt += 1
                totalCnt += lastCnt
                i += 1
            elif ratings[i] == ratings[i - 1]:
                cnt, i = calcDesc(i, float("inf"))
                totalCnt += cnt
                lastCnt = 1
            else:
                cnt, i = calcDesc(i, lastCnt)
                totalCnt += cnt
                lastCnt = 1
        
        return totalCnt
            
