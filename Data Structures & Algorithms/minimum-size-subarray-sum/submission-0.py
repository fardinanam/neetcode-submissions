class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        nums = [0] + nums

        # 0 2 3 8 9 14 17

        l, r = 0, 1
        res = len(nums)
    
        while l <= r < len(nums):
            if nums[r] - nums[l] < target:
                r += 1
            else:
                if r - l < res:
                    res = r - l
    
                l += 1
        
        return res if res < len(nums) else 0