class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]

        heapq.heapify(maxHeap)

        prev = None
        res = ''

        while len(res) < len(s):
            if prev and not maxHeap:
                return ''

            cnt, char = heapq.heappop(maxHeap)
            res += char

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            cnt += 1
            
            if cnt != 0:
                prev = [cnt, char]
        
        return res

