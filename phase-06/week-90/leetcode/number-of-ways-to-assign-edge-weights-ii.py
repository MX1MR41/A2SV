# Binary lifting + dp + bfs
# Binary lifiting is a technique used to efficiently traverse up an acyclic tree from any node
# hence, finding the LCA of any two nodes (must be located on the same level) becomes very efficient.
# For every node, precompute the ancestor located at a distance of every power of 2
# i.e. for node x, find its ancestors at steps 1, 2, 4...  upto the allowed distance and store them in map
# then to find the ancestor of node x at any distance d, we keep jumping up by every largest possible power
# of 2 until we reach the ancestor at distance d. This works because any number can be represented in binary
# hence any distance can be covered by choosing spcific powers of 2, taking the largest you can at any time.
# To find the LCA of any two nodes, those two nodes must first be on the same level because we will be 
# jumping the same amount for both hence we need them to exist and move in parallel. 
# Then we keep moving by the largest power of 2 possible, possible as in moving by this much doesn't 
# reach an LCA yet so we need to cover this much distance anyways. We keep repeating this 
# jumping-by-the-largest-power-of-2 process and it is guaranteed we reach an LCA.
# As for the finding the distance between any two nodes, once we know the LCA of the two nodes and we know
# the depth of the LCA and those two nodes, algebra got it.
# As for the dynamic programming part, refer to the first version of this problem.(it is precomputed here)
# In short, this problem can be broken down into find the LCA of any two nodes efficiently, find the distance
# between them, compute the number of ways for that distance. 



MOD = 10**9 + 7
n = 10**5

ways = [0 for _ in range(n + 1)]
ways[1] = 1
for i in range(2, n + 1):
    ways[i] = (2 * ways[i - 1]) % MOD


class Lifter:
    def __init__(self, edges, root):
        self.root = root
        self.graph = defaultdict(list)
        self.depth = defaultdict(int)

        # self.ancestory[node_x][distance_d] = ancestor_of_node_x_at_distance_d
        self.ancestor = defaultdict(lambda: defaultdict(lambda: None))

        # 1) Build graph
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)


        # 2) Precompute the depth of each node, and its parent(ancestor at distance 1) using BFS
        que = deque([(self.root, None)])
        seen = set([self.root])

        lev = 0
        while que:
            for _ in range(len(que)):
                u, p = que.popleft()
                self.depth[u] = lev
                self.ancestor[u][1] = p

                for v in self.graph[u]:
                    if v in seen:
                        continue

                    seen.add(v)
                    que.append((v, u))

            lev += 1


        # 3) Move down the tree using BFS, computing the ancestors of each node at power of 2 distances
        que = deque([self.root])
        seen = set([self.root])

        while que:
            for _ in range(len(que)):
                u = que.popleft()
                dep = self.depth[u]

                if dep > 0: # log2 doesn't accept 0

                    # to find the the ancestor a_1 at distance 2^x, 
                    # we can jump to ancestor a_1 located at 2^(x - 1) then from there by 2^(x - 1) much
                    # so 2^(x - 1) + 2^(x - 1) = 2^(x - 1)(1 + 1) = 2^(x - 1)(2) = 2^x
                    # by the time we compute for node x, we would've already computed for all its ancestors
                    # and by the time we compute for i, we would have already computed for all upto i - 1
                    for i in range(1, floor(log2(dep)) + 1):

                        half = 2**(i - 1) # same as 2**i//2

                        half_ancestor = self.ancestor[u][half]

                        self.ancestor[u][2**i] = self.ancestor[half_ancestor][half]

                for v in self.graph[u]:
                    if v in seen:
                        continue

                    seen.add(v)
                    que.append(v)



    def lift(self, node, steps):
        curr = node
        
        # keep jumping up by the largest power of 2 possible
        while steps > 0:

            if steps in self.ancestor[curr]: # found ancestor since it was precomputed
                return self.ancestor[curr][steps]

            less_steps = 2 ** floor(log2(steps))

            curr = self.ancestor[curr][less_steps]

            steps -= less_steps

        return curr



    def LCA(self, u, v):

        dep = self.depth[u]

        if u == v:
            return u

        # keep jumping by the largest power of two possible, process can be transformed to
        # check all possible powers of 2 in descending order and see which ones you can use
        # you can use/jump via the ones that don't let you reach an LCA yet
        for i in range(floor(log2(dep)), -1, -1):
            steps = 2**i
            ua = self.ancestor[u][steps]
            va = self.ancestor[v][steps]

            if ua != va:
                u = ua
                v = va

        return self.ancestor[u][1]


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        lifter = Lifter(edges, 1)

        max_depth = max(lifter.depth.values())

        dists = []
        for u, v in queries:
            iu = u
            iv = v
            depu = lifter.depth[u]
            depv = lifter.depth[v]
            
            # bring them up to the same level
            if depu > depv:
                diff = depu - depv
                u = lifter.lift(u, diff)
            if depv > depu:
                diff = depv - depu
                v = lifter.lift(v, diff)


            LCA = lifter.LCA(u, v) 
            dist = lifter.depth[iu] + lifter.depth[iv] - 2 * lifter.depth[LCA]
            dists.append(dist)

        res = []
        for d in dists:
            w = ways[d]
            res.append(w)

        return res









# UnionFind + dp + bfs + dfs
# The hardest part of this problem is still finding the LCA of any two nodes efficiently
# We can use Tarjan's offline LCA algorithm 
# This algorithm depends on all the queries being known beforehand, and compute the LCA of each query
# in one DFS, hence offline (unlike binary lifting which does online computation as queries come on the fly)
# This algorithm exploits the nature of DFS, more specifically the post-traversal kind. 
# During DFS, we explore a tree branch by branch. It naturally follows that for two nodes located in
# different branches their LCA will be where those branches are rooted at. 
# To reach some node v in a branch, we must've came down the tree, came down the LCA root to 
# a previous branch, finsihed exploring that branch, then went back up to the LCA,
# then went down the new/other current branch to node v. If there was a query for v and some other node u
# located in a previous branch, then the answer would be the sub-tree's root which is still being explored
# so we somehow need to associate the nodes of the previously explored branch to that sub-tree root.
# We could do that by using UnionFind: once we finsihed exploring that branch, we union it with that sub-root
# and we can make the (dsu) root of that group to be that sub-root. Then when we are at node v and want to 
# query it with u, we just need to find the dsu root of u, which we assigned the sub-root as.
# So in essence, we union branches to a sub-root when we finish exploring the branches so that for other nodes
# in other branches we can easily find the root of the divergent branches.
# The unionfind will weight the root by the least depth (instead of most rank or most size) so that dsu groups
# will be rooted at sub-roots


MOD = 10**9 + 7
n = 10**5

ways = [0 for _ in range(n + 1)]
ways[1] = 1
for i in range(2, n + 1):
    ways[i] = (2 * ways[i - 1]) % MOD


class UnionFind:
    def __init__(self, depth):
        self.root = {}
        self.depth = depth

    def find(self, x):
        if x not in self.root:
            self.root[x] = x

        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]

    def union(self, u, v):
        rootu = self.find(u)
        rootv = self.find(v)

        if rootu == rootv:
            return

        du = self.depth[rootu]
        dv = self.depth[rootv]

        # make the ancestor the root
        if du <= dv:
            self.root[rootv] = rootu
        else:
            self.root[rootu] = rootv


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        depth = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        que = deque([1])
        seen = set([1])
        d = 0

        while que:
            for _ in range(len(que)):
                u = que.popleft()

                depth[u] = d

                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        que.append(v)

            d += 1

        dsu = UnionFind(depth)

        LCAS = [None for _ in range(len(queries))]

        qs = [(ind, u, v) for ind, (u, v) in enumerate(queries)]
        qmap = defaultdict(list)
        for ind, u, v in qs:
            qmap[u].append((v, ind))
            qmap[v].append((u, ind))


        seen = set()


        def dfs(u):

            seen.add(u)

            # go over queries that have have u in them and find their LCA
            for v, ind in qmap[u]:
                if v not in seen:
                    continue

                LCA = dsu.find(v)
                LCAS[ind] = LCA

            # go down the branches
            for v in graph[u]:
                if v in seen:
                    continue

                dfs(v)
                
                # union once we finsihed exploring the branch and returned from exploring it
                dsu.union(u, v)


        dfs(1)

        res = []
        for ind, (u, v) in enumerate(queries):
            LCA = LCAS[ind]

            dist = depth[u] + depth[v] - 2 * depth[LCA]

            w = ways[dist]
            res.append(w)

        return res
