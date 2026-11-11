class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]

        for num in nums:
            count[num] += 1
        
        nums[: count[0]] = [0] * count[0]
        nums[count[0]: count[0] + count[1]] = [1] * count[1]
        nums[count[0] + count[1]:] = [2] * count[2]
                