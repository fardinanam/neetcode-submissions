class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        t = []

        for trip in trips:
            t.append([trip[1], trip[0]])
            t.append([trip[2], -trip[0]])
        
        t.sort()

        passengers = 0

        for trip in t:
            passengers += trip[1]

            if passengers > capacity:
                return False

        return True