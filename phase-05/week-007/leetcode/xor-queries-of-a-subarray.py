class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [arr[0]]
        p = arr[0]
        for i in arr[1:]:
            p ^= i
            pre.append(p)


        
        ans = []
        for l, r in queries:
            if l == r:
                ans.append(arr[l])
                continue

            if l == 0:
                ans.append(pre[r])
                continue

            ans.append(pre[r]^pre[l-1])

        return ans

        
