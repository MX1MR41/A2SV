class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2
            papers = n - mid

            if citations[mid] == papers:
                return papers
            elif citations[mid] < papers:
                l = mid + 1
            else:
                r = mid - 1
        
        return n - l  