class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left, right = 0, mountainArr.length() - 1
        peak = peakLeft = peakRight = -1
        mid = (left + right) // 2
        
        while left < right:
            midVal = mountainArr.get(mid)

            if midVal == target:
                return mid
            
            midLeftVal = mountainArr.get(mid - 1)
            midRightVal = mountainArr.get(mid + 1)

            if midLeftVal < midVal and midRightVal < midVal:
                peak = mid
                peakLeft = left
                peakRight = right

                right = mid
            elif target < midVal and midLeftVal < midVal \
                    or target > midVal and midLeftVal > midVal:
                right = mid
            else:
                left = mid + 1
            
            mid = (left + right) // 2
        
        if mountainArr.get(mid) == target:
            return mid
        
        if peak != -1:
            left = peak + 1
            right = peakRight
            mid = (left + right) // 2

            while left < right:

                midVal = mountainArr.get(mid)

                if midVal == target:
                    return mid
            
                if target < midVal:
                    left = mid + 1
                else:
                    right = mid

                mid = (left + right) // 2
        
        if mountainArr.get(mid) == target:
            return mid

        return -1

