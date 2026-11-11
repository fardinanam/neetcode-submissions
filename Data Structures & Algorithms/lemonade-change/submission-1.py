class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = [0, 0, 0]

        for bill in bills:
            if bill == 5:
                changes[0] += 1
            elif bill == 10:
                if not changes[0]:
                    return False
                changes[0] -= 1
                changes[1] += 1
            else:
                if changes[1] and changes[0]:
                    changes[0] -= 1
                    changes[1] -= 1
                elif changes[0] > 2:
                    changes[0] -= 3
                else:
                    return False
                changes[2] += 1
        
        return True