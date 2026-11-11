class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustCounts = [0 for i in range(n)]

        for t in trust:
            trustCounts[t[1] - 1] += 1
        
        judge = -1
        for i, trustCount in enumerate(trustCounts):
            if trustCount >= n - 1:
                judge = i + 1
        
        for t in trust:
            if t[0] == judge:
                judge = -1
                break
        
        return judge