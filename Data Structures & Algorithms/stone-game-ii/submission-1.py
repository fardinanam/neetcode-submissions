class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}

        def dfs(i, m, isAlice):
            if i >= n:
                return 0

            if (i, m, isAlice) in dp:
                return dp[(i, m, isAlice)]

            res = 0 if isAlice else float("inf")
            s = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break

                s += piles[i + x - 1]

                if isAlice:
                    res = max(res, s + dfs(i + x, max(m, x), not isAlice))
                else:
                    res = min(res, dfs(i + x, max(m, x), not isAlice))
            
            dp[(i, m, isAlice)] = res
            return res
        
        return dfs(0, 1, True)