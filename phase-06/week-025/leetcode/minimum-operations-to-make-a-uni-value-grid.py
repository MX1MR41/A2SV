class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # greedy
        # if an answer exists, it is gonna be the median(s)
        # so we need to only check those values

        def check(target):
            steps = 0
            for i in arr:
                diff = abs(target - i)
                if diff % x:

                    return [False, float("inf")]

                steps += diff // x

            return [True, steps]

        arr = []
        for row in grid:
            arr += row

        arr.sort()
        n = len(arr)
        if n == 1:
            return 0
        if n % 2:
            a = arr[n // 2]
            res1 = check(a)
            b = arr[n // 2 + 1]
            res2 = check(b)
            if res1[0] and res2[0]:
                return min(res1[1], res2[1])
            elif res1[0]:
                return res1[1]
            elif res2[0]:
                return res2[1]
            else:
                return -1
        else:
            a = arr[n // 2]
            res = check(a)

            if res[0]:
                return res[1]
            else:
                return -1
