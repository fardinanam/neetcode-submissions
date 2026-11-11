class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        if l1 < l2 and str1 != str2[:l1] \
            or l1 > l2 and str2 != str1[:l2] \
            or l1 == l2 and str1 != str2:
            print("line 7")
            return ""
        
        if l1 == l2:
            return str1
        
        den = 1

        while den <= min(l1, l2):
            l = min(l1, l2) // den
            if min(l1, l2) % l:
                den += 1
                continue
            
            s = str1[: l1 // den] if l1 < l2 else str2[: l2 // den]

            # print(s)
            l = len(s)
            if s * (l1 // l) == str1 and s * (l2 // l) == str2:
                return s

            den += 1

        return ""
