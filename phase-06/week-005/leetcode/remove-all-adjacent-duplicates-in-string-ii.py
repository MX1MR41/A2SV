class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack
        # instead of storing every element occurence, store an element with frequency
        stk = []
        for i in s:
            if stk and stk[-1][0] == i:
                i, cnt = stk.pop()
                cnt += 1
                if cnt == k:
                    continue

                elif cnt < k:
                    stk.append((i, cnt))

            else:
                stk.append((i, 1))


        ans = ""
        for i, cnt in stk:
            ans += i*cnt

        return ans
        
