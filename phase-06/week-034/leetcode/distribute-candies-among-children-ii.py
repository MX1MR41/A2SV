class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # after choosing x1, rem = n - x1
        # for x2 and x3 we need them to be
        # 1) x2 + x3 = rem
        # 2) 0 <= x2 <= limit
        # 3) 0 <= x3 <= limit
        # From (1), x3 = rem - x2. Substitute this into (3):
        # 0 <= rem - x2 <= limit
        # This gives two inequalities for x2:
        # a. rem - x2 >= 0 => x2 <= rem
        # b. rem - x2 <= limit => x2 >= rem - limit

        ans = 0

        for i in range(min(n, limit) + 1):

            rem = n - i

            min_candies_for_x2 = max(0, rem - limit)
            max_candies_for_x2 = min(rem, limit)

            curr = 0
            if min_candies_for_x2 <= max_candies_for_x2:

                curr = max_candies_for_x2 - min_candies_for_x2 + 1

            ans += curr

        return ans
