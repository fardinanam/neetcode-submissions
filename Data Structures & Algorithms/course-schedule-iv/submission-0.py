class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adjList[prerequisite[0]].append(prerequisite[1])
        
        p = [set() for _ in range(numCourses)]
        visited = [False] * numCourses

        def dfs(u):
            if visited[u]:
                return p[u]
            
            for v in adjList[u]:
                p[u].add(v)
                p[u] = p[u] | dfs(v)
            
            visited[u] = True
            return p[u]

        for u in range(numCourses):
            if not visited[u]:
                dfs(u)
        
        res = []

        for query in queries:
            res.append(query[1] in p[query[0]])
        
        return res



