"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    # recursive approach
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)


        for emp in employees:
            graph[emp.id].append(emp.importance)
            graph[emp.id].append(emp.subordinates)

        # print(graph)

        def dfs(ID, visited):
            if ID in visited: return 0
            # print(graph[ID])
            visited.add(ID)
            tot, subs = graph[ID]
            # print("tot:",tot)
            # print("subs:",subs)
            for sub in subs:
                tot += dfs(sub, visited)

            return tot

        return dfs(id, set())



class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # iterative approach
        graph = defaultdict(list)

        for emp in employees:
            graph[emp.id].append(emp.importance)
            graph[emp.id].append(emp.subordinates)


        stk = [id]
        visited = set()

        res = 0
        while stk:
            ID = stk.pop()
            if ID in visited: continue
            visited.add(ID)
        
            imp, subs = graph[ID]
            res += imp
            for sub in subs:
                stk.append(sub)
            

        return res
                



        

        

        

        
