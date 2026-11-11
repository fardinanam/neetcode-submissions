class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k - 1

        for i in range(k, len(arr)):
            if abs(x - arr[i]) < abs(x - arr[l]):
                r = i
                l = r - k + 1
        
        return arr[l: r + 1]

