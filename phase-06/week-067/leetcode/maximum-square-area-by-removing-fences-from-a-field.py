class Solution:
    def maximizeSquareArea( self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # to form a square we need equal units both horizontally and vertically
        # there are gaps in between fences which are the initial units we have
        # we simulate removal of a fence by summing up the gaps on either side of the fence
        # so the problem can be reframed as finding the largest subarray sum in both the 
        # horizontal and vertical gaps array


        hFences.sort()
        vFences.sort()

        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]

        vGaps = []
        for i in range(1, len(vFences)):
            vGaps.append(vFences[i] - vFences[i - 1])

        hGaps = []
        for i in range(1, len(hFences)):
            hGaps.append(hFences[i] - hFences[i - 1])

        sums = set()

        max_area = -1

        for i in range(1, len(vGaps)):
            vGaps[i] += vGaps[i - 1]

        for i in range(1, len(hGaps)):
            hGaps[i] += hGaps[i - 1]

        for i in range(len(vGaps)):
            for j in range(i, len(vGaps)):
                sub_sum = vGaps[j] - vGaps[i - 1] if i > 0 else vGaps[j]
                sums.add(sub_sum)

        for i in range(len(hGaps)):
            for j in range(i, len(hGaps)):
                sub_sum = hGaps[j] - hGaps[i - 1] if i > 0 else hGaps[j]
                if sub_sum in sums:
                    max_area = max(max_area, sub_sum**2)

        return max_area % 1000000007 if max_area != -1 else -1
