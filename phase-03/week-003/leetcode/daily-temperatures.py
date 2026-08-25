class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [] # monotonic decreasing stack
        res = [0 for _ in range(len(temperatures))]
        for i, day in enumerate(temperatures):
            while stk and stk[-1][-1] < day:
                last = stk.pop()
                res[last[0]] = i - last[0]
                
            stk.append((i,day))
            

        return res


        