class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        last = customers[0][0]
        ave = 0
        for arrive, time in customers:
            tot = max(last, arrive) + time
            ave += tot - arrive
            last = tot


        return (ave/len(customers))

        
