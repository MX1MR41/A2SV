class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # topological sort coupled with dynamic programming
        # vanilla topological sort won't work because some courses could
        # start(when all their pre's are done) and finish earlier than their
        # topologically equivalent peers (i.e. layer).
        # So we compute the end time of each pre then store it for in all of its courses
        # when we get to a course, we find the biggest end time from its pre's and then compute 
        # and store its end time using that info.
        indeg = defaultdict(int)
        g = defaultdict(list)
        for pre, course in relations:
            g[pre].append(course)
            indeg[course] += 1

        que = deque()
        for i in range(1, n + 1):
            if indeg[i] == 0:
                que.append((i, 0))

        end_times = defaultdict(int)
        past_end_times = defaultdict(list)

        def bfs(que):
            while que:
          
                for _ in range(len(que)):
                    curr, start = que.popleft()
                    end_time = start + time[curr - 1]
                    end_times[curr] = end_time

                    neis = g[curr]
                    for nei in neis:
                        past_end_times[nei].append(end_time)
                        indeg[nei] -= 1
                        if indeg[nei] == 0:
                            que.append((nei, max(past_end_times[nei])))

        bfs(que)
        ans = 0

        for i in range(1, n + 1):
            ans = max(ans, end_times[i])

        return ans
