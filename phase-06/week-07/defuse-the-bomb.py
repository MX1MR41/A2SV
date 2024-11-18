class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0]*n
        elif k > 0:
            ans = []
            for i in range(n):
                tot = 0
                nxt = 1
                while nxt <= k:
                    tot += code[(i + nxt) % n]
                    nxt += 1

                ans.append(tot)

            return ans

        else:
            ans = []
            for i in range(n):
                tot = 0
                prev = -1
                while prev >= k:
                    tot += code[(i + prev) % n]
                    prev -= 1

                ans.append(tot)

            return ans
