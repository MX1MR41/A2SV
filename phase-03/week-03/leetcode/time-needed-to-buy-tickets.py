class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        kth = tickets[k]
        time = 0
        while kth > 0:
            for i in range(n):
                if i == k:
                    kth -= 1
                    if not kth:
                        time += 1
                        return time
                if not tickets[i]:
                    continue
                tickets[i] -= 1
                time += 1


            
        