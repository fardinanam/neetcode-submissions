class Solution:
    def merge(self, nums: List[int], start: int, mid: int, end: int):
        temp = []

        i = start
        j = mid + 1
        
        while i <= mid and j <= end:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        
        if i <= mid:
            temp = temp + nums[i: mid + 1]
        if j <= end:
            temp = temp + nums[j: end + 1]
        
        nums[start: end + 1] = temp


    def sortArrayIdx(self, nums: List[int], start: int, end: int):
        if start >= end:
            return
        
        mid = (start + end) // 2

        self.sortArrayIdx(nums, start, mid)
        self.sortArrayIdx(nums, mid + 1, end)

        self.merge(nums, start, mid, end)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.sortArrayIdx(nums, 0, len(nums) - 1)
        return nums