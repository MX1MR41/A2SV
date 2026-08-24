class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # binary search + backtracking + combinatorics
        # we use binary search over the list of all possible multiples
        # to find the smallest multiple which has k multiples upto it
        # to count how many multiples there are upto a number x, we need to use
        # the inclusion-exclusion principle. Since we have multiple coins there will be
        # common multiples shared between different groups of coins, so we need to count the unique
        # total multiples in the set without overcounting. We do that by the formula.
        # For example for 4 elements, the formula will be 
        # (A + B + C + D) - (AB + AC + AD + BC + BD) + (ABC + ABD + BCD) - (ABCD)
        # where each variable represents the total number of unique multiples there for that specifc
        # group i.e. A means total multiples of A upto X, 
        # AB means total common multiples of A and B upto x, and so on
        # For any combination of coins, the number of common multiples upto x is equal to x // LCM

        # remove unnecessary coins which are multiples of already existing coins
        coins.sort()
        n = len(coins)
        removed = set()
        for i in range(n - 1, -1, -1):
            curr = coins[i]
            found = False
            for j in range(i - 1, -1, -1):
                prev = coins[j]
                if curr % prev == 0:
                    found = True
                    break

            if found:
                removed.add(curr)

        coins = [i for i in coins if i not in removed]

        # enumerate all possible combinations of coins along with their LCMs
        lcms = defaultdict(int)

        def backtrack(ind, chosen, curr_lcm):
            if ind == len(coins):
                return

            new_lcm = lcm(curr_lcm, coins[ind])
            new_chosen = chosen | (1 << ind)

            group = tuple(coins[i] for i in range(len(coins)) if new_chosen & (1 << i))

            lcms[group] = new_lcm
            backtrack(ind + 1, new_chosen, new_lcm)
            backtrack(ind + 1, chosen, curr_lcm)

        backtrack(0, 0, 1)


        # calculate the n'th part of the inclusion-exclusion formula
        def incExc(n, x):
            keys = [key for key in lcms if len(key) == n]
            total = 0
            for key in keys:
                curr_lcm = lcms[key]
                common_multiples = x // curr_lcm
                total += common_multiples

            return total


        # count the total multiples upto x
        def countLesser(x):
            count = 0
            sign = 1
            # manually build the inclusion-exclusion formula, 
            # by gathering the sums of all length groups
            # and by alternating signs as well
            for i in range(1, len(coins) + 1):
                count += sign * incExc(i, x)
                sign *= -1

            return count


        # binary search over the answer space
        maxx = coins[-1] * k
        res = maxx
        c = coins[-1]
        l, r = 1, maxx

        while l <= r:
            mid = (l + r) // 2

            cnt = countLesser(mid)
            if cnt >= k:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res


