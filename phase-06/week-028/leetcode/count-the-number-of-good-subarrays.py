# Solution 1
class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        # [frequency of x, number of pairs that can be formed by all the x's]
        self.tree = [[0, 0] for _ in range(2 * self.n)]

    def update(self, x, v):
        x += self.n

        self.tree[x][0] += v
        # arithmetic progression formula to count how many pairs could be formed
        # (n*(n + 1))//2 pairs can be formed from n + 1 nums
        # or ((n - 1)*n)//2 pairs can be formed from n nums
        self.tree[x][1] = (self.tree[x][0] * (self.tree[x][0] - 1)) // 2

        x = x // 2 if not x % 2 else (x - 1) // 2

        while x > 0:
            self.tree[x][1] = self.tree[2 * x][1] + self.tree[2 * x + 1][1]
            x = x // 2 if not x % 2 else (x - 1) // 2


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # segment tree
        # use segment tree to calculate the number of pairs over all the nums
        # since nums could get upto 10**9, our segment tree can't be instantiated as
        # large as the biggest num in nums. Instead, since the size of nums won't
        # exceed 10**5, we can sort the nums and assign each of them as an index
        # from 0 to 10**5, that way our segment tree will be small enough but contain
        # all necessary info about all the numbers in nums

        sorted_nums = sorted(nums)
        n = len(nums)
        offset_indices = {}
        for i in range(n):
            num = sorted_nums[i]
            if num not in offset_indices:
                offset_indices[num] = i

        tree = SegmentTree(n + 1)

        res = 0
        l = 0
        for r in range(n):
            rnum = offset_indices[nums[r]]
            tree.update(rnum, 1)

            # we just need to query the top of the segment tree which will have the 
            # total number of pairs
            while tree.tree[1][1] >= k:
                res += n - r
                lnum = offset_indices[nums[l]]
                tree.update(lnum, -1)
                l += 1

        return res

# Solution 2

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # sliding window
        # when we add a new occurence of a number x into the window, we need to 
        # recompute x's individual contribution to the total number of pairs
        # we do that by deducting the contribution it had with its previous frequency
        # and adding the new contribution it will have with its new frequency.
        # The same logic applies, but in reverse, when we remove an element from window
        # A number x with frequency f contributes (f*(f - 1))//2 pairs 
        pairs = 0
        res = 0
        freq = defaultdict(int)

        l = 0
        n = len(nums)
        for r in range(n):
            rnum = nums[r]
            last_freq = freq[rnum]
            new_freq = last_freq + 1
            freq[rnum] = new_freq

            pairs -= (last_freq*(last_freq - 1))//2
            pairs += (new_freq*(new_freq - 1))//2

            while pairs >= k:
                res += n - r #every subsequent subarray that includes this one is valid

                lnum = nums[l]
                last_freq = freq[lnum]
                new_freq = last_freq - 1
                freq[lnum] = new_freq

                pairs -= (last_freq*(last_freq - 1))//2
                pairs += (new_freq*(new_freq - 1))//2

                l += 1

        return res
                    
        
