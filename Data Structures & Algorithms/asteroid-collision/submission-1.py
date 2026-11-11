class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for asteroid in asteroids:
            destroyed = False
            while res and not destroyed and res[-1] > 0 and asteroid < 0:
                if res[-1] < -asteroid:
                    res.pop()
                elif res[-1] == -asteroid:
                    res.pop()
                    destroyed = True
                else:
                    destroyed = True

            if not destroyed:
                res.append(asteroid)
        
        return res

