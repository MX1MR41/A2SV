class Solution:
    def minSwaps(self, s: str) -> int:
        # count opening and closing brackets as you go
        # if closing > opening, swap and bring one opening from beyond and remove a closing
        o = c = 0
        swaps = 0

        for i in s:
            if i == "[":
                o += 1
            else:
                c += 1

            if c > o:
                swaps += 1
                o += 1
                c -= 1

        return swaps
        
