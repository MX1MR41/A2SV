class UnionFind:
    def __init__(self):
        self.root = dict()
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.root:
            self.root[x] = x
            return x

        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return

        rankx, ranky = self.rank[rootx], self.rank[rooty]
        if rankx < ranky:
            self.root[rootx] = rooty
        elif rankx > ranky:
            self.root[rooty] = rootx
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1

class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        # unionfind + prefix sum + greedy
        # for each letter, find the interval within which it is inside a special
        # substring where every letter in that substring shouldn't exist elsewhere.
        # if letters x and y coincide like this [x....y..x...y] then their special
        # substring is from the first x upto the last y. So for every letter, get the
        # first and last index of that letter as s and e, then for every 
        # other letter if it exists between s and e BUT ALSO exists outside s and e,
        # we group these two letters into the same group to indicate that their 
        # special interval is the same one. Then for every group, minimize its start
        # by finding the earliest index of one of its letters, and maximize its end
        # by finding the last index of one of its letters. At the end, the group's
        # start and end indicates an inclusive special substring for all its letters.
        # To find out which letters exist within s and e, use prefix sum where
        # prefix[i] = a frequency array of all the letters upto index i.
        # while iterating, if we exhausted the last index of a letter (reached e),
        # we get prefix[s], then use it to calculate the freqs of letters from s to e
        # if the freq of a certain letter is > 0 and it's last index hasn't been 
        # reached yet, that means ther is an overlap, so we union the two letters
        # Then, to maximize the number of intervals, use a greedy approach where we
        # always select the earliest ending interval, and discard overlapping ones.

        start = dict()
        end = dict()

        n = len(s)

        for i in range(n):
            if s[i] not in start:
                start[s[i]] = i

            end[s[i]] = i


        letters = list(set(s))

        dsu = UnionFind()

        cnt = Counter(s)
        curr = Counter()

        prefix = []

        freq = [0] * 26

        ended = [False] * 26

        for i in s:
            curr[i] += 1

            ind = ord(i) - 97
            freq[ind] += 1

            prefix.append(freq[:])

            if curr[i] == cnt[i]:
                ended[ind] = True


            if ended[ind]:
                start_ind = start[i]
                prev_prefix = prefix[start_ind]

                diff = [freq[l] - prev_prefix[l] for l in range(26)]

                for l in range(26):
                    if ended[l]:
                        diff[l] = 0

                    if diff[l] > 0:
                        dsu.union(i, chr(l + 97))



        root_start_end = defaultdict(lambda : [float("inf"), float("-inf")])

        for i in letters:
            root = dsu.find(i)
            root_start_end[root][0] = min(root_start_end[root][0], start[i])
            root_start_end[root][1] = max(root_start_end[root][1], end[i])

        for i in letters:
            root = dsu.find(i)
            s, e = root_start_end[root]
            start[i] = s
            end[i] = e


        intervals = list((start[i], end[i]) for i in letters)

        intervals.sort(key = lambda x: x[::-1])

        res = [intervals[0]]

        for s, e in intervals[1:]:
            if s > res[-1][-1]:
                res.append((s, e))


        if len(res) == 1 and res[0] == (0, n - 1):
            return False if k > 0 else True

        return len(res) >= k
