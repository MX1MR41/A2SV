class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = Counter()
        for dom in dominoes:
            dom = (min(dom), max(dom))
            cnt[dom] += 1


        res = 0
        for dom, freq in cnt.items():
            res += freq * (freq - 1)//2

        return res
