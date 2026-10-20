class SegmentTree:
    def __init__(self, n, is_min):
        self.is_min = is_min
        self.n = 2 ** ceil(log2(n))
        self.tree = [0 for _ in range (2 * self.n)]

    def updatePoint(self, ind, x):
        ind += self.n
        self.tree[ind] = x

        ind = ind // 2 if not ind % 2 else (ind - 1)//2

        while ind > 0:
            left = self.tree[2 * ind]
            right = self.tree[2 * ind + 1]
            if right == 0:
                self.tree[ind] = left
            elif left == 0:
                self.tree[ind] = right
            else:
                if self.is_min:
                    self.tree[ind] = min(right, left)
                else:
                    self.tree[ind] = max(right, left)

            ind = ind//2 if not ind % 2 else (ind - 1)//2

    def queryRange(self, l, r):
        if self.is_min:
            res = float("inf")
            func = min
        else:
            res = 0
            func = max

        l += self.n
        r += self.n

        while l <= r:
            if l % 2:
                res = func(res, self.tree[l])
                l = (l + 1)//2
            else:
                l //= 2

            if not r % 2:
                res = func(res, self.tree[r])
                r = (r - 2)//2
            else:
                r = (r - 1)//2

        if l == r:
            res = func(self.tree[l], res)

        return res

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        # segment tree + prefix sum
        n = len(nums)

        minTree = SegmentTree(n, True)
        maxTree = SegmentTree(n, False)

        spikes = 0
        pre = []
        for i in range(n):
            if i > 0 and nums[i] < nums[i - 1]:
                spikes += 1
            pre.append(spikes)

            minTree.updatePoint(i, nums[i])
            maxTree.updatePoint(i, nums[i])

        res = 0
        for i in range(1, n + 1):
            if n % i != 0:
                continue

            valid = True
            prev_max = float("-inf")
            for j in range(i - 1, n, i):
                l, r = j - i + 1, j

                spikes = pre[r] - pre[l]
                
                if spikes > 1 or (spikes == 1 and nums[r] > nums[l]):
                    valid = False
                    break

                curr_min = minTree.queryRange(l, r)
                if curr_min < prev_max:
                    valid = False
                    break

                curr_max = maxTree.queryRange(l, r)
                prev_max = curr_max

            if valid:
                res += i

        return res
