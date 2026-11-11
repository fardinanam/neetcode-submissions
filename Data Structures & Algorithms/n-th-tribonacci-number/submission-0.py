class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1

        tn = [-1] * (n + 1)

        tn[0] = 0
        tn[1] = tn[2] = 1

        for i in range(3, n + 1):
            tn[i] = tn[i - 1] + tn[i - 2] + tn[i - 3]
        
        return tn[-1]
