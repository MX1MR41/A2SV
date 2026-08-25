class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        freq = defaultdict(list)
        for num, f in cnt.items():
            freq[f].append(num)

        temp = []
        for f, items in sorted(freq.items(), key = lambda x: x[0]):
            temp += sorted(items, reverse = True)

        res = []
        for num in temp:
            res += [num] * cnt[num]

        
        return res

        
