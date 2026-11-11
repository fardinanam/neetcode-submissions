class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = [0] * 26

        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        res = ''

        while len(res) != len(s):
            maxChar = ''
            maxCount = 0

            for i in range(26):
                if counts[i] > maxCount and (len(res) == 0 or len(res) > 0 \
                    and i != ord(res[-1]) - ord('a')):
                    maxCount = counts[i]
                    maxChar = chr(i + ord('a'))
            
            if maxChar == '':
                return ''

            res += maxChar
            counts[ord(maxChar) - ord('a')] -= 1
        
        return res
