class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k % len(nums) != 0:
            k = k % len(nums)
            nums[:k], nums[k:] = nums[-k:], nums[:-k]

        