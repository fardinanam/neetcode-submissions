class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a:
            heapq.heappush(heap, [-a, 'a'])
        if b:
            heapq.heappush(heap, [-b, 'b'])
        if c:
            heapq.heappush(heap, [-c, 'c'])

        res = ''
        carry = None

        while heap:
            count, char = heapq.heappop(heap)

            if len(res) >= 2 and char == res[-1] == res[-2]:
                carry = [count, char]
            else:
                res += char

                if count < -1:
                    heapq.heappush(heap, [count + 1, char])

                if carry:
                    heapq.heappush(heap, carry)
                    carry = None
        
        return res
