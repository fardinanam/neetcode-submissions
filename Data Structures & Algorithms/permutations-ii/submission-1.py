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
            if len(current) == len(nums):
                res.append(current.copy())
                return
            
            for key in counts:
                if counts[key] == 0:
                    continue
    
                current.append(key)
                counts[key] -= 1
                
                dfs()
        
                counts[key] += 1
                current.pop()
        
        dfs()
        return res
