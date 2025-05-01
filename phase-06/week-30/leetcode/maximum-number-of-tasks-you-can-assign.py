class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # binary search + binary search + greedy
        tasks.sort()
        workers.sort()

        def check(k: int) -> bool:
            task = tasks[:k]
            task.reverse()
            work = workers[-k:]
            p = pills

            for t in task:

                if work and work[-1] >= t:
                    work.pop()
                    continue

                if p == 0:
                    return False

                idx = bisect_left(work, t - strength)
                if idx == len(work):
                    return False

                work.pop(idx)
                p -= 1

            return True

        l, r = 0, min(len(tasks), len(workers))
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
