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
        p = [i for i in range(len(nums))]

        def find(i):
            if p[i] == i:
                return i

            p[i] = find(p[i])

            return p[i]
            
        
        def union(i, j):
            if p[i] == p[j]:
                return
            
            pi = find(i)
            pj = find(j)

            p[p[i]] = pj
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if self.gcd(nums[i], nums[j]) > 1:
                    union(i, j)
            
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if find(i) != find(j):
                    return False
        
        return True
