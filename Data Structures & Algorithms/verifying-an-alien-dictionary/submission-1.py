class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lexOrd = { ch: i for i, ch in enumerate(order) }

        for i in range(1, len(words)):
            if len(words[i - 1]) > len(words[i]) and words[i - 1][:len(words[i])] == words[i]:
                return False

            for j in range(min(len(words[i - 1]), len(words[i]))):
                if lexOrd[words[i - 1][j]] < lexOrd[words[i][j]]:
                    break
                elif lexOrd[words[i - 1][j]] > lexOrd[words[i][j]]:
                    return False
                
                j += 1   

            i += 1

        return True