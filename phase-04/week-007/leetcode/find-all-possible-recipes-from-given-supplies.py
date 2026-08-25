class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # classic topological sort problem where nodes are sorted by their indegrees
        # in this case by their ingredients
        # start from your supplies in a queue and for every supply remove its edges
        # and if a recipe happened to have an indegree of 0 after edge removal 
        # (i.e. made from its ingredients), we add it into the queue and continue the process
        res = []
        indeg = defaultdict(int)
        g = defaultdict(list)

        n = len(recipes)

        for i in range(n):
            rec, ings = recipes[i], ingredients[i]
            for j in ings:
                g[j].append(rec)
                indeg[rec] += 1

        que = deque(supplies)

        while que:
            for _ in range(len(que)):
                node = que.popleft()

                neis = g[node]

                for nei in neis:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        que.append(nei)
                        res.append(nei)



        return res

        
