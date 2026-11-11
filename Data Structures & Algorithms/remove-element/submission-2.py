class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        left, right = 0, len(nums) - 1

        while left <= right:
            while right >= 0 and nums[right] == val:
                right -= 1
                k -= 1
            
            if left <= right and nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]

            left += 1 
        return k