class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)

        def sign(i, j):
            diff = arr[i] - arr[j]
            if diff == 0:
                return 0

            return int(diff / abs(diff))
        
        maxLen = 1
        prevSign = 0
        currLen = 1

        for i in range(len(arr) - 1):
            currSign = sign(i, i + 1)
            if currSign == 0:
                currLen = 1
            elif currSign == prevSign:
                currLen = 2
            else:
                currLen += 1

            if currLen > maxLen:
                maxLen = currLen

            prevSign = currSign
            
        
        return maxLen


