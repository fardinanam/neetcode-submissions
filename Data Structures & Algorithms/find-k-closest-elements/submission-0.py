class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closestIdx = -1
        closest = 10001

        for i, num in enumerate(arr):
            if abs(num - x) < abs(closest - x):
                closestIdx = i
                closest = num
        
        res = deque([closest])
        k -= 1
        l, r = closestIdx - 1, closestIdx + 1
        while k > 0:
            if 0 <= l and r < len(arr):
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    res.appendleft(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l < 0:
                res.append(arr[r])
                r += 1
            else:
                res.appendleft(arr[l])
                l -= 1
            
            k -= 1

        return list(res)