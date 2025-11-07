# SOLUTION 1
# Python code fails due to python overhead, but c++ version passes
# logic is correct and asymptotically it is valid
class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)

    def update_point(self, ind, val):
        ind += self.n

        self.tree[ind] += val

        ind = ind // 2 if not ind % 2 else (ind - 1) // 2

        while ind > 0:
            self.tree[ind] = self.tree[2 * ind] + self.tree[2 * ind + 1]
            ind = ind // 2 if not ind % 2 else (ind - 1) // 2

    def query_range(self, l, r):
        tot = 0
        l += self.n
        r += self.n

        while l <= r:
            if l % 2:
                tot += self.tree[l]
                l = (l + 1) // 2
            else:
                l //= 2

            if not r % 2:
                tot += self.tree[r]
                r = (r - 2) // 2
            else:
                r = (r - 1) // 2

        return tot


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # binary search + segment tree
        # need to find the maximum minimum, hence can be solved using binary search
        # where a check function checks if a given value x can be a minimum,
        # and the binary search part quickly find the last valid (maximum) minimum
        # in the check function, we need an efficient way to update a point and
        # query a range because the power of a city is the sum of the range of (i-r,i+r)
        # for that we can use segment tree. 
        # while checking for a value x, if a city's power is less than x, we add as many
        # power stations we can to increase its power to exactly x.
        # the newly added power stations will be stationed at i + r, i.e. the furthest 
        # city possible so that we can simultaneously help as many future cities possible

        width = r

        def check(x):
            arr = stations[:]
            n = len(arr)
            curr_k = k

            tree = SegmentTree(n)

            # populate seg tree
            for i in range(n):
                tree.update_point(i, arr[i])

            for i in range(n):
                l = max(0, i - width)
                r = min(n - 1, i + width)

                power = tree.query_range(l, r)

                if power < x:
                    need = x - power
                    if need > curr_k: # can't bring the power to x, so x can't be minimum
                        return False

                    curr_k -= need

                    arr[r] += need
                    tree.update_point(r, need)

            return True

        res = 0
        l, r = 0, sum(stations) + k

        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res





# SOLUTION 2
# Much more optimized by replacing functionality of segment trees by prefix sum arrays

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # binary search + prefix sum
        # same concept as the segment tree solution
        # we precompute a prefix sum array to compute range sums of initial stations
        # we allocate another preix sum array 'added' that will contain the cumulative
        # sum of NEWLY added stations due to modifications, and it will be updated
        # point by point as the for loop iterates. 
        # At any point (city), we will need to know the range sum up to i+r, 
        # so we will be update added[i+r] for every i we visit by doing 
        # added[i+r] += added[i+r-1]... simple prefix summing up


        width = r


        def check(x):
            curr_k = k

            pre = stations[:]
            
            n = len(pre)

            for i in range(1, n):
                pre[i] += pre[i - 1]

            added = [0] * n
            for i in range(n):
                l = max(0, i - width)
                r = min(n - 1, i + width)
                
                # necessary condition so we don't re-add at the ends of the array
                if i + width < n: 
                    added[i + width] += added[i + width - 1] 

                if l > 0:
                    right = pre[r] + added[r] # intial stations plus newly added stations
                    left = pre[l - 1] + added[l - 1]
                    power = right - left
                else:
                    right = pre[r] + added[r]
                    power = right


                if power < x:
                    need = x - power
                    if curr_k < need:
                        return False

                    added[r] += need # add at the furthest city possible

                    curr_k -= need

                

            return True




        res = 0
        l, r = 0, sum(stations) + k

        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res
