class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or k == 0:
            return False

        if nums[0] == nums[1]:
            return True
        
        found = {nums[0], nums[1]}
        l, r = 0, 2

        while l < r < len(nums):
            if abs(l - r) > k:
                found.remove(nums[l])
                l += 1
            
            if nums[r] in found:
                return True
            
            found.add(nums[r])
            r += 1
        
        return False