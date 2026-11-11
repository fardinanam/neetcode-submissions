class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
    
        tasks.sort()
        tasks = deque(tasks)

        time = tasks[0][0]
        heap = []

        while tasks and tasks[0][0] == time:
            heapq.heappush(heap, tasks[0][1:])
            tasks.popleft()

        res = []

        while heap:
            processingTask = heapq.heappop(heap)
            time += processingTask[0]
            res.append(processingTask[1])

            if not heap and tasks and time < tasks[0][0]:
                time = tasks[0][0]

            while tasks and tasks[0][0] <= time:
                heapq.heappush(heap, tasks[0][1:])
                tasks.popleft()

        return res