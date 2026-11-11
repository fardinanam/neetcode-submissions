class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        currXor = 0

        def recurse(i):
            nonlocal currXor, res
            if i == len(nums):
                res += currXor
                return
            
            recurse(i + 1)
            currXor ^= nums[i]
            recurse(i + 1)
        
        recurse(0)
        return res