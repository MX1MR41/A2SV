class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # classic min-max max-min question that can be solved using binary search
        # search space is the the set of possible outputs i.e. possible force vals

        n = len(position)

        # function to check if a given distance/force is valid
        def check(dist):
            last = position[0]
            balls = m - 1

            for i in range(1, n):
                if position[i] - last >= dist:
                    last = position[i]
                    balls -= 1
                    if balls == 0:
                        return True

            return False

        position.sort()
        ans = 0
        l, r = 1, position[-1] - position[0]

        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
