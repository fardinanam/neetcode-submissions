class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lexOrd = dict()

        for i, ch in enumerate(order):
            lexOrd[ch] = i
        
        i = 1

        while i < len(words):
            j = 0

            if len(words[i - 1]) > len(words[i]) and words[i - 1][:len(words[i])] == words[i]:
                return False

            while j < min(len(words[i - 1]), len(words[i])):
                if lexOrd[words[i - 1][j]] < lexOrd[words[i][j]]:
                    break
                if lexOrd[words[i - 1][j]] > lexOrd[words[i][j]]:
                    return False
                
                j += 1   

            i += 1

        return True