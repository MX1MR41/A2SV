class UnionFind:
    def __init__(self):
        self.root = defaultdict(str)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x]) 
        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if rootx <= rooty:
                self.root[y] = rootx
                for i in self.root:
                    if self.root[i] == rooty:
                        self.root[i] = rootx
            else:
                self.root[x] = rooty
                for i in self.root:
                    if self.root[i] == rootx:
                        self.root[i] = rooty


    

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # use unionfind to merge accounts of the same owner into one set
        # represented by the lexicographically smallest email
        owner = defaultdict(str) # owner of a given email
        dsu = UnionFind()

        for acc in accounts:
            for email in acc[1:]:
                owner[email] = acc[0] # set the owner of the email
                if not dsu.root[email]: # hasn't been processed yet
                    dsu.root[email] = email 

            n = len(acc)
            for i in range(1, n-1): # union accounts side by side
                dsu.union(acc[i], acc[i+1])


        # unpack the disjoint sets
        emails = defaultdict(set)
        for email in dsu.root:
            rep = dsu.root[email]
            emails[rep].add(email)

        res = []
        for email in emails:
            acc = []

            own, ems = owner[email], emails[email]
            
            acc.extend([*ems])
            acc.sort()
            
            res.append([own, *acc])

        return res


        
