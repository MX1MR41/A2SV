from collections import defaultdict
import sys, threading
input = lambda: sys.stdin.readline().strip()

def main():

    class UnionFind:
        def __init__(self, n):
            self.root = {i:i for i in range(1, n+1)}
            self.rank = defaultdict(int)

            self.min = {i:i for i in range(1, n+1)}
            self.max = {i:i for i in range(1, n+1)}
            self.len = {i:1 for i in range(1, n+1)}

        def _min(self, x):
            rootx = self.find(x)
            return self.min[rootx]
        def _max(self, x):
            rootx = self.find(x)
            return self.max[rootx]
        def _len(self, x):
            rootx = self.find(x)
            return self.len[rootx]

        def find(self, x):
            if x != self.root[x]:
                self.root[x] = self.find(self.root[x])

            return self.root[x]
        
        def union(self, x, y):
            rootx, rooty = self.find(x), self.find(y)
            rankx, ranky = self.rank[rootx], self.rank[rooty]


            if rootx != rooty:
                _min = min(self._min(rootx), self._min(rooty))
                _max = max(self._max(rootx), self._max(rooty))
                _len = self._len(rootx) + self._len(rooty)

                if rankx < ranky:
                    self.root[rootx] = rooty
                elif rankx > ranky:
                    self.root[rooty] = rootx
                else:
                    self.root[rootx] = rooty
                    self.rank[x] += 1


                self.min[rootx] = self.min[rooty] = _min
                self.max[rootx] = self.max[rooty] = _max
                self.len[rootx] = self.len[rooty] = _len

    n, m = list(map(int, input().split()))
    dsu = UnionFind(n)

    for _ in range(m):
        inp = input().split()

        if "union" in inp:
            x, y = list(map(int, inp[1:]))
            dsu.union(x, y)

        else:
            x = int(inp[-1])
            print(dsu._min(x), dsu._max(x), dsu._len(x))


        
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

