class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # math + binary search
        # the number of operations per number change at every power of 4
        # i.e. from 0 to 0 = 1, 1 to 3 = 1, 4 to 15 = 2, 16 to 63 = 3
        # we only need upto 4**15 because log(10**9, 4) = 15
        # construct array points where points[i] is the first power of 4 which requires
        # i operations to be reduced to zero. Then for ever [l, r] in queries
        # find the total number of operations required for that range by systematically
        # traversing over the points array. Start from l then find in which points segment
        # it belongs, then compute the length from l to end of that segment and add i * 
        # length because  every element in that segment requires i operations. Then traverse
        # to the start of the next segment and repeat until you reach r.
        # once the total operations required for a range are figured out, we divide by two
        # since we can take a pair at a time

        points = [0, 1]
        for i in range(15):
            points.append(points[-1] * 4)

        def find_in_range(x):
            l, r = 0, len(points) - 1
            res = l
            while l <= r:
                mid = (l + r) // 2
                if points[mid] <= x:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1

            return res

        def range_ops(l, r):
            num = l
            tot_ops = 0
            while num <= r:
                ind = find_in_range(num)

                if ind == len(points) - 1:
                    curr_range = r - num + 1
                    curr_ops = ind * curr_range
                    tot_ops += curr_ops
                    break

                end = min(r, points[ind + 1] - 1)
                curr_range = end - num + 1
                curr_ops = ind * curr_range
                tot_ops += curr_ops

                num = end + 1

            return tot_ops



        res = 0

        for l, r in queries:

            res += ceil(range_ops(l, r) / 2)

        return res
