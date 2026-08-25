class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # prefix sum + binary search
        
        max_beauty_prefix = []
        n = len(items)
        items.sort()
        _max = 0
        for i in range(n):
            _max = max(_max, items[i][1])
            max_beauty_prefix.append(_max)


        ans = []

        for q in queries:
            l, r = 0, n - 1
            best = 0
            while l <= r:
                mid = (l + r)//2
                if items[mid][0] <= q:
                    best = mid
                    l = mid + 1
                else:
                    r = mid - 1
            
            if items[best][0] <= q:
                ans.append(max_beauty_prefix[best])
            else:
                ans.append(0)

        return ans


        
