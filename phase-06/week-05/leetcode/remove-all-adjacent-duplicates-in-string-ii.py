class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for i in s:
            if stk and stk[-1][0] == i:
                i, cnt = stk.pop()
                cnt += 1
                if cnt == k:
                    continue
                elif cnt > k:
                    stk.append((i, cnt - k))

                elif cnt < k:
                    stk.append((i, cnt))

            else:
                stk.append((i, 1))


        ans = ""
        for i, cnt in stk:
            ans += i*cnt

        return ans
        
