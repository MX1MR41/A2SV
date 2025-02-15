class Solution:
    def punishmentNumber(self, n: int) -> int:
        # backtracking
        def dfs(num):
            if num == "":
                return 0

            tot = [int(num)]

            for i in range(1, len(num)):
                curr = num[:i]
                curr = int(curr) if curr else 0
                curr_list = []
                nxt = dfs(num[i:])

                for n in nxt:
                    tot.append(curr + n)

            return tot

        tot = 0
        for i in range(1, n + 1):
            res = dfs(str(i*i))
            if i in res:
                tot += i*i

        return tot
                

        
