class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            if len(count) == 3:
                new_count = defaultdict(int)
                for key, val in count.items():
                    if val > 1:
                        new_count[key] = val - 1
                
                count = new_count
        
        res = []
        for key, _ in count.items():
            if nums.count(key) > len(nums) // 3:
                res.append(key)
        
        return res