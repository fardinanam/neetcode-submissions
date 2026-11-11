class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        mid = (low + high) // 2

        while low < high:
            count = 0
            currSum = 0

            for weight in weights:
                currSum += weight
                if currSum > mid:
                    currSum = weight
                    count += 1
                
                if count > days:
                    low = mid + 1
                    break

            count += 1
            if count > days:
                low = mid + 1
            else:
                high = mid
            
            mid = (low + high) // 2
    
        return mid