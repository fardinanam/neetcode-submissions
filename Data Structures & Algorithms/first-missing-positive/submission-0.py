class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        heapq.heapify(nums)

        smallest = 1

        while nums:
            num = heapq.heappop(nums)
            if num <= 0:
                continue

            if num > smallest:
                break
            
            smallest = num + 1
        
        return smallest