class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # prefix sum
        # we can consider each num as a range (num - k, num + k)
        # we want to find the maximum overlap of ranges
        # we can create an array that will act as a number line where we plot our ranges
        # then we count the maximum overlap

        ranges = [(i - k, i + k) for i in nums]

        _min = _max = 0
        for start, end in ranges:
            _min = min(_min, start, end)
            _max = max(_max, start, end)

        # in case we have a negative number, we will need to offset all nums
        # so that our nums stay greater than 0
        offset = 0
        if _min < 0:
            offset = abs(_min)

        prefix_sum = [0] * (_max - _min + 2)

        for start, end in ranges:
            left = start + offset # start of the range
            right = end + offset # end of the range


            prefix_sum[left] += 1 # we have one more range that starts at left
            prefix_sum[right + 1] -= 1 # and ends just after right

        # build the prefix sum array
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i - 1]

        return max(prefix_sum)
