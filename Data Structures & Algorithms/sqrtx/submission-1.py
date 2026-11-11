class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        l, r = 1, (x // 2) + 1
        m = (l + r) // 2
        while l < r:
            guess = m * m

            if guess == x:
                return m
            
            if guess < x:
                l = m + 1
            else:
                r = m
            
            m = (l + r) // 2
        
        return m if m * m <= x else m - 1
