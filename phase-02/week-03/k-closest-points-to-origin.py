class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        # store each point along with its distance as a list
        arr = [[p[0], p[1], sqrt(p[0]**2 + p[1]**2)] for p in points]
        # sort by their distance 
        arr.sort(key = lambda x: x[-1])

        for i in range(k):
            ans.append(arr[i][:-1])

        return ans