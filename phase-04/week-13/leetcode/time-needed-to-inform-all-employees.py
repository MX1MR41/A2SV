class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        

        def dfs(node):
            curr = informTime[node]
            time = 0
            neis = g[node]
            for nei in neis:
                temp = dfs(nei)
                if temp: 
                    time = max(time, temp)

            return curr + time



        g = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                g[manager[i]].append(i)

        return dfs(headID)
        
