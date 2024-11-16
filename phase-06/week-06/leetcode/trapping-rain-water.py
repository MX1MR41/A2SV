class Solution:
    def trap(self, height: List[int]) -> int:
        # dp
        # precompute and store the max heights from the left and right
        # for each height h, there will be water as high as the shortest of its left_max
        # and right_max minus the height of this block itself
        n = len(height)
        left_max = []
        right_max = []

        m = 0
        for h in height:
            m = max(h, m)
            left_max.append(m)

        m = 0
        for h in height[::-1]:
            m = max(h, m)
            right_max.append(m)

        right_max.reverse()

        water = 0

        for i in range(n):
            h = height[i]
            water += max(0, min(left_max[i], right_max[i]) - h)

        return water
