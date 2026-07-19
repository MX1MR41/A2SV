
        # monotonic stack
        # build a monotonic sequence and pop from stack only if the popped exists later
        n = len(s)
        exists_after = [[False for _ in range(26)]]
        for i in range(n - 1, 0, -1):
            exists_after.append(exists_after[-1][:])
            exists_after[-1][ord(s[i]) - ord('a')] = True

        exists_after.reverse()

        stk = [s[0]]
        in_stk = Counter()
        in_stk[s[0]] = 1
        for i in range(1, n):
            curr = s[i]
            if in_stk[curr] == 0:

                while (
                    stk 
                    and curr < stk[-1] 
                    and exists_after[i][ord(stk[-1]) - ord('a')]
                    ):
                    in_stk[stk.pop()] -= 1


                stk.append(curr)
                in_stk[curr] += 1

        return "".join(stk)
        
