class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        walls.sort()
        n = len(robots)
        dist = {robots[i]:distance[i] for i in range(n)}

        robots.sort()
        set_w = set(walls)
        # print("walls =  ", walls)
        # print("robots = ", robots)
        # print("dist =   ", [dist[i] for i in robots])

        dp = [[0, 0] for _ in range(n)]

        def count(left, right):
            if left > right:
                return 0

            start = len(walls)
            
            l = 0
            r = len(walls) - 1
            while l <= r:
                mid = (l + r)//2
                if walls[mid] >= left:
                    start = mid
                    r = mid - 1
                else:
                    l = mid + 1

            end = -1

            l = 0
            r = len(walls) - 1
            while l <= r:
                mid = (l + r)//2
                if walls[mid] <= right:
                    end = mid
                    l = mid + 1
                else:
                    r = mid - 1


            return max(0, end - start + 1)




        l = robots[0] - dist[robots[0]]
        r = robots[0] + dist[robots[0]]



        dp[0][0] = count(l, robots[0] - 1)
        dp[0][1] = (
            count(robots[0] + 1, min(r, robots[1] - 1)) 
            if n > 1 
            else count(robots[0] + 1, r)
        )
        
        prev_right = dp[0][1]

        if robots[0] in set_w:
            dp[0][0] += 1
            dp[0][1] += 1




        for i in range(1, n):
            l = robots[i] - dist[robots[i]]
            r = robots[i] + dist[robots[i]]

            between = count(robots[i - 1] + 1, robots[i] - 1)

            left_gain = count(max(robots[i - 1] + 1, l), robots[i] - 1)

            rem = between - left_gain
            debt = prev_right - rem

            # print(f"{between = } {left_gain = } {rem = } {prev_right = } {debt = }")

            dp[i][0] = max(
                dp[i - 1][0] + left_gain,
                dp[i - 1][1] + left_gain - max(0, debt)
            )


            right_gain = (
                count(robots[i] + 1, min(r, robots[i + 1] - 1))
                if i + 1 < n
                else count(robots[i] + 1, r)
            )

            dp[i][1] = right_gain + max(dp[i - 1])
            prev_right = right_gain

            if robots[i] in set_w:
                dp[i][0] += 1
                dp[i][1] += 1

        # print(dp)

        return max(dp[-1])

        
       
