class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # heap
        cnt = Counter(s)
        multi = []
        single = []
        for x, f in cnt.items():
            if f > 1:
                heappush(multi, (x, f))
            else:
                heappush(single, x)


        left = right = ""

        while multi:
            x, f = heappop(multi)

            left += x
            right += x

            f -= 2

            if f > 1:
                heappush(multi, (x, f))
            elif f == 1:
                heappush(single, x)

        while single:
            left += heappop(single)

        return left + right[::-1]

        
