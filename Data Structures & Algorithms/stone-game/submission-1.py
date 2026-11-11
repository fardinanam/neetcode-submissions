class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        sumPiles = sum(piles)

        dp = dict()

        def dfs(l, r):
            if (l, r) in dp:
                return dp[(l, r)]

            if l == r:
                return 0
        
            left = dfs(l + 1, r) + piles[l]
            right = dfs(l, r - 1) + piles[r]

            dp[(l, r)] = left if left > right else right
            return dp[(l, r)]
        
        return True if dfs(0, len(piles) - 1) > sumPiles // 2 else False