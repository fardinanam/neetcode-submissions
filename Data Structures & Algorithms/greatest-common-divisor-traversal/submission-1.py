class Solution:
    def gcd(self, a, b):
        if a < b:
            a, b = b, a

        while b != 0:
            r = a % b
            a = b
            b = r

        return a
    
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        p = [i for i in range(n)]
        rank = [1] * n
        comps = n

        def find(i):
            if p[i] == i:
                return i

            p[i] = find(p[i])

            return p[i]
            
        
        def union(i, j):
            nonlocal comps
            pi = find(i)
            pj = find(j)

            if p[i] == p[j]:
                return

            if rank[i] < rank[j]:
                p[pi] = pj
                rank[pj] += rank[pi]
            else:
                p[pj] = pi
                rank[pi] += rank[pj]
            
            comps -= 1

        factor_idx = {}
        for i, num in enumerate(nums):
            f = 2
            while f * f <= num:
                if not num % f:
                    if f in factor_idx:
                        union(i, factor_idx[f])
                    else:
                        factor_idx[f] = i
                
                    while not num % f:
                        num = num // f
                
                f += 1
            
            if num > 1:
                if num in factor_idx:
                    union(i, factor_idx[num])
                else:
                    factor_idx[num] = i

        
        return comps == 1
