class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        counts = dict()

        for num in nums:
            if num not in counts:
                counts[num] = 0

            counts[num] += 1
        
        current = []

        def dfs():
            if not counts:
                res.append(current.copy())
                return
            
            keys = list(counts.keys())
            for key in keys:
                current.append(key)
                counts[key] -= 1

                if counts[key] == 0:
                    del counts[key]
                
                dfs()

                if key not in counts:
                    counts[key] = 0
        
                counts[key] += 1
                current.pop()
        
        dfs()
        return res
