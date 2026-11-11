class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        curr = nums[0]
        count = 1
        res = []

        for i in range(1, len(nums)):
            if nums[i] == curr:
                count += 1
            else:
                if count > len(nums) // 3:
                    res.append(curr)
                
                curr = nums[i]
                count = 1
        
        if (len(res) == 0 or res[-1] != curr) \
            and count > len(nums) // 3:
            res.append(curr)
    
        return res