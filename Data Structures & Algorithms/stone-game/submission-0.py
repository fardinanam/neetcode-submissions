class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        sumPiles = sum(piles)

        dp = dict()

        def dfs(l, r, currTotal):
            if (l, r, currTotal) in dp:
                return dp[(l, r, currTotal)]

            if l == r or currTotal > sumPiles // 2:
                dp[(l, r, currTotal)] = currTotal
                return currTotal
        
            left = dfs(l + 1, r, currTotal + piles[l])
            right = dfs(l, r - 1, currTotal + piles[r])

            dp[(l, r, currTotal)] = left if left > right else right
            return dp[(l, r, currTotal)]
        
        return True if dfs(0, len(piles) - 1, 0) > sumPiles // 2 else False