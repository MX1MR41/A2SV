class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:

        arr = [1 if x % modulo == k else 0 for x in nums]

        pre = defaultdict(int)
        pre[0] = 1

        res = 0
        p = 0

        for v in arr:
            p += v

            need = (p - k) % modulo
            res += pre[need]

            pre[p % modulo] += 1

        return res
