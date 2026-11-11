class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] < x:
                l = m + 1
            else:
                r = m - 1
        
        m = l

        if l > 0 and abs(x - arr[l - 1]) < abs(x - arr[m]):
            m = l - 1
        
        if l < len(arr) - 1 and abs(x - arr[l + 1]) < abs(x - arr[m]):
            m = l + 1

        # print(arr[m])
        l = max(0, m - k + 1)
        r = l + k - 1

        while r + 1 < m + k and r + 1 < len(arr) \
            and abs(x - arr[r + 1]) < abs(x - arr[l]):
            l += 1
            r += 1
        
        return arr[l: r + 1]
            
            

