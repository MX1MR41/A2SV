class Solution:
    def clearStars(self, s: str) -> str:
        # heap
        heap = []
        removed = set()

        n = len(s)
        for i in range(n):
            curr = s[i]
            if curr == "*":
                last, last_ind = heappop(heap)
                removed.add(-last_ind)
                removed.add(i)

            else:
                heappush(heap, (s[i], -i))

        res = ""
        for i in range(n):
            if i not in removed:
                res += s[i]

        return res

        
