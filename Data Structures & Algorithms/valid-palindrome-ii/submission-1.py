class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r and s[l] == s[r]:
            l += 1
            r -= 1

        if l >= r:
            return True
        
        l1, r1 = l + 1, r
        misMatched = False

        while l1 < r1:
            if s[l1] != s[r1]:
                misMatched = True
            l1 += 1
            r1 -= 1

        l1, r1 = l, r - 1

        while l1 < r1:
            if s[l1] != s[r1] and misMatched:
                return False
            l1 += 1
            r1 -= 1

        return True