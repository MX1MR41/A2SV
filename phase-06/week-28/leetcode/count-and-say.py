class Solution:
    def countAndSay(self, n: int) -> str:
        # recursion
        if n == 1:
            return "1"

        temp = self.countAndSay(n - 1)

        rle = []

        for i in temp:
            if not rle:
                rle.append([1, i])
                continue

            if i == rle[-1][-1]:
                rle[-1][0] += 1
            else:
                rle.append([1, i])

        res = ""
        for cnt, i in rle:
            res += str(cnt) + i

        return res

            

        
