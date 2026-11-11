class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {}

        n = len(words)

        if n == 1:
            return words[0]

        for i in range(n - 1):
            w1 = words[i]
            w2 = words[i + 1]
            found_at = -1

            for j in range(min(len(w1), len(w2))):
                if w1[j] not in adj_list:    
                    adj_list[w1[j]] = set()
                if w2[j] not in adj_list:
                    adj_list[w2[j]] = set()
                if w1[j] != w2[j] and found_at == -1:
                    adj_list[w1[j]].add(w2[j])
                    found_at = j
            
            if found_at == -1 and len(w1) > len(w2):
                return ''

            if found_at < len(w1) - 1:
                for j in range(found_at + 1, len(w1)):
                    if w1[j] not in adj_list:    
                        adj_list[w1[j]] = set()
            if found_at < len(w2) - 1:
                for j in range(found_at + 1, len(w2)):
                    if w2[j] not in adj_list:    
                        adj_list[w2[j]] = set()

        visited = {}
        s = deque()

        # print(adj_list)

        def dfs(a):
            if a not in visited:
                visited[a] = 1
            elif visited[a] == 1:
                return False
            elif visited[a] == 2:
                return True

            for b in adj_list[a]:
                if not dfs(b):
                    return False
                
            visited[a] = 2

            s.append(a)
            return True
        
        for key in adj_list:
            if key not in visited:
                if not dfs(key):
                    return ''
        
        res = ''
        while s:
            res += s.pop()
        return res
        
