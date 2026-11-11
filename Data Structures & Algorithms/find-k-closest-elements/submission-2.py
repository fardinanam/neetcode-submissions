class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque(arr[:k])

        for i in range(k, len(arr)):
            if abs(x - arr[i]) < abs(x - res[0]):
                res.popleft()
                res.append(arr[i])
        
        return list(res)

