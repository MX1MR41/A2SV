class Fancy:
    def __init__(self):
        self.MOD = 1000000007
        self.seq = []
   
        self.a = 0
        self.m = 1

        self.prev_a = defaultdict(int)
        self.prev_m = defaultdict(lambda : 1)

    def append(self, val: int) -> None:
        self.seq.append(val)
        ind = len(self.seq) - 1

        self.prev_a[ind] = self.a
        self.prev_m[ind] = self.m

    def addAll(self, inc: int) -> None:
        self.a += inc

    def multAll(self, m: int) -> None:
        self.m *= m
        self.a *= m

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1

        num = self.seq[idx]

        tot_m = self.m // self.prev_m[idx]
        
        
        tot_a = self.a - (self.prev_a[idx] * tot_m)

        
        return (num * tot_m + tot_a) % self.MOD
