class Solution:
    def simplifyPath(self, path: str) -> str:
        res = ['/']

        i = 0

        while i < len(path):
            if path[i] == '/':
                if res and res[-1] != '/':
                    res.append('/')
            else:
                j = i + 1
                while j < len(path) and path[j] != '/':
                    j += 1
                
                word = path[i:j]
                if j - i == 2 and word == '..' and len(res) >= 2:
                    res.pop()
                    res.pop()
                elif word != '.' and word != '..':
                    res.append(path[i:j])
                
                i = j - 1

            i += 1
        
        if len(res) > 1 and res[-1] == '/':
            res.pop()

        return ''.join(res)