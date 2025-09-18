# heap
# keep track of the priorities and users of each task in dictionaries
# store the (-priority, -taskId, userId) thruple in a heap to quickly find the highest priority task
# whenever a task's priority is edited, add the (-newPriority, -taskId, userId) thruple into the heap
# redundant and inaccurate thruples will be deleted from the heap in a lazy manner whenever
# execTop() is called
# delete the taskId from the users and prioriies dictionaries whenever a task is removed 

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_priority = dict()
        self.task_user = dict()
        self.task_heap = []

        for userId, taskId, priority in tasks:
            self.task_priority[taskId] = priority
            self.task_user[taskId] = userId

            heappush(self.task_heap, (-priority, -taskId, userId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_priority[taskId] = priority
        self.task_user[taskId] = userId
        
        heappush(self.task_heap, (-priority, -taskId, userId))


    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_priority[taskId] = newPriority
        userId = self.task_user[taskId]

        heappush(self.task_heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        del self.task_priority[taskId]
        del self.task_user[taskId]

    def execTop(self) -> int:

        while self.task_heap and (
            (-self.task_heap[0][1] not in self.task_priority)
            or (self.task_priority[-self.task_heap[0][1]] != -self.task_heap[0][0])
            or (self.task_user[-self.task_heap[0][1]] != self.task_heap[0][2])
        ):
            heappop(self.task_heap)

        if not self.task_heap:
            return -1

        priority, taskId, userId = heappop(self.task_heap)

        del self.task_priority[-taskId]
        del self.task_user[-taskId]

        return userId
