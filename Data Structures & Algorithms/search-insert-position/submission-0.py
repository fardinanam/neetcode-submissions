class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        m = (l + r) // 2
        while l < r:

            if target == nums[m]:
                return m

            if target < nums[m]:
                r = m
            else:
                l = m + 1
            
            m = (l + r) // 2

        return m