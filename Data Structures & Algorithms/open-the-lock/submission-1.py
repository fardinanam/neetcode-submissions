class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque(["0000"])
        visited = set(["0000"])
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        count = 0
        p = dict()
        p[target] = -1
        p['0000'] = 0

        while q:
            u = q.popleft()

            for i in range(4):
                d = int(u[i])

                v = u
                v = u[:i] + str((d + 1) % 10) + u[i + 1:]

                if v not in deadends and v not in visited:
                    p[v] = p[u] + 1
                    q.append(v)
                
                visited.add(v)

                v = u[:i] + str((d - 1) % 10) + u[i + 1:]

                if v not in deadends and v not in visited:
                    p[v] = p[u] + 1
                    q.append(v)
                
                visited.add(v)

        
        return p[target]
