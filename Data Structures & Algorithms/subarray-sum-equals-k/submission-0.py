class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1

        s = 0
        count = 0

        for i in range(len(nums)):
            s += nums[i]

            required = s - k

            if required in sums:
                count += sums[required]

            sums[s] += 1

        return count