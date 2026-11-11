class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pivot = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot = i

        print(pivot)
        l, r = 0, len(nums) - 1

        if nums[0] <= target <= nums[pivot]:
            l, r = 0, pivot
        else:
            l, r = pivot + 1, len(nums) - 1
        
        if l >= len(nums):
            return False

        while l < r:
            m = (l + r) // 2

            if nums[m] == target:
                return True
    
            if target < nums[m]:
                r = m
            else:
                l = m + 1

        if nums[l] == target:
            return True
        
        return False