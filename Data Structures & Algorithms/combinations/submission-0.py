class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(i, k):
            if n - i + 1 < k:
                return
    
            if k == 0:
                res.append(comb.copy())
                return
            
            comb.append(i)
            dfs(i + 1, k - 1)
            comb.pop()
            dfs(i + 1, k)

        dfs(1, k)
        return res