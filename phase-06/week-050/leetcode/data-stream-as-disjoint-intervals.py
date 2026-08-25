# segment tree + merge intervals
# instead of a sum segment tree, keep track of the interval within the range of a given node
# when building a node's intervals, perform merge intervals over the combined intervals of 
# its left and right children

class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [[] for _ in range(2 * self.n)]

    def add(self, value):
        ind = value
        ind += self.n
        self.tree[ind] = [[value, value]]
        ind = ind // 2 if not ind % 2 else (ind - 1) // 2

        while ind > 0:
            left_intervals = self.tree[2 * ind]
            right_intervals = self.tree[2 * ind + 1]

            merged = left_intervals + right_intervals
            intervals = []
            for i in range(len(merged)):
                if not merged[i]:
                    continue

                l, r = merged[i]
                if not intervals:
                    intervals.append([l, r])
                    continue

                if l == intervals[-1][1] + 1:
                    prev_l, _ = intervals.pop()
                    intervals.append([prev_l, r])
                else:
                    intervals.append([l, r])

            self.tree[ind] = intervals

            ind = ind // 2 if not ind % 2 else (ind - 1) // 2

    def getIntervals(self):
        return self.tree[1]


class SummaryRanges:

    def __init__(self):
        self.tree = SegmentTree(10**4)

    def addNum(self, value: int) -> None:
        self.tree.add(value)

    def getIntervals(self) -> List[List[int]]:

        return self.tree.getIntervals()
