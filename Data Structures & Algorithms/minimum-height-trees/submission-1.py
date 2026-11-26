class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(n)]

        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        leaves = deque()
        edge_cnt = {}

        for src, neighbors in enumerate(adjList):
            if len(neighbors) <= 1:
                leaves.append(src)
            
            edge_cnt[src] = len(neighbors)
        

        while leaves:
            if n <= 2:
                break
            
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1

                for neighbor in adjList[node]:
                    edge_cnt[neighbor] -= 1

                    if edge_cnt[neighbor] == 1:
                        leaves.append(neighbor)
                    

        return list(leaves)
        
