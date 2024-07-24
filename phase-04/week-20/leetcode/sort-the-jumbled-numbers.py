class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = defaultdict(int)
        for i in range(len(mapping)):
            mapped[i] = mapping[i]

        def mapper(num):
            num = str(num)
            ans = ""
            for i in num:
                ans += str(mapped[int(i)])

            return int(ans)

        nums.sort(key = lambda x: mapper(x))
        return nums


        
