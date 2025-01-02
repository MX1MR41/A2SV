class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # prefix sum
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        def vowelString(word):
            return word[0] in vowels and word[-1] in vowels

        prefix_sum = []
        pre = 0
        for word in words:
            if vowelString(word):
                pre += 1

            prefix_sum.append(pre)

        res = []
        for l, r in queries:
            if l == 0:
                res.append(prefix_sum[r])
            else:
                res.append(prefix_sum[r] - prefix_sum[l - 1])

        return res
        
