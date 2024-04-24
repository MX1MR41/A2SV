class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # the solution works by using a heap to keep track of which next available task 
        # has a shorter processing time, as well as smaller index
        n = len(tasks)

        for ind, task in enumerate(tasks):
            # since we might need to compare tasks with similar processing time by their indices,
            # we need to store the indices of each task as well in the array itself.
            # storing them in a dictionary instead has edge cases
            task.insert(1, ind)

        # sorting them based on enqueue time
        tasks.sort()
        # task will keep track of the next index in the array,
        # and time is initialized as the first task's enqueue time
        task, time = 0, tasks[0][0]
        heap, res = [], []

        # this function, given the current time after processing one task, adds all tasks 
        # whose enque time is less than or equal to the current given time.
        def tasker(time):
            nonlocal task, heap, tasks
            # meaning the CPU is idle and no task has been enqueued yet
            if task < n and time < tasks[task][0]:
                # meaning if there are still items in our heap whose enqueue time was
                # sometime before the given time, we do nothing and just let the CPU
                # process the pending tasks stored in the heap
                if heap: return time

                # meaning that the CPU has no pending tasks, so we can fast-forward
                else: time = tasks[task][0]

            while task < n and tasks[task][0] <= time:
                enq, ind, d_time = tasks[task]
                # store processing time, index, enque time in that order, cuz of their precedence
                heappush(heap, (d_time, ind, enq))
                task += 1

            return time

        tasker(time)

        while heap:
            d_time, ind, enq = heappop(heap)
            # this task has been finished
            res.append(ind)

            time += d_time
            
            time = tasker(time)

        return res
