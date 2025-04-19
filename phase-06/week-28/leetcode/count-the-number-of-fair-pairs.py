# Solution 1

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # sorting + binary search
        # for each num, find the the first next num which would make their sum >= lower
        # and find last next num which would make their sum <= upper
        # the number of elements in between (hi - lo + 1) are all the valid choices
        # sorting the nums won't cause issue because nums[i] + nums[j] == nums[j] + nums[j]
        # counting for either nums[i] or nums[j] will suffice not to count for the other
        n = len(nums)
        count = 0
        nums.sort()


        for i in range(n - 1):
            l, r = i + 1, n - 1
            hi, lo = l, r

            while l <= r:
                mid = (l + r)//2
                if nums[mid] + nums[i] >= lower:
                    lo = mid
                    r = mid - 1
                else:
                    l = mid + 1

            l, r = i + 1, n - 1
            while l <= r:
                mid = (l + r)//2
                if nums[mid] + nums[i] <= upper:
                    hi = mid
                    l = mid + 1
                else:
                    r = mid - 1


            if lower <= nums[i] + nums[lo] and nums[i] + nums[hi] <= upper:
                count += hi - lo + 1

        return count
            
            


# Solution 2

class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)

    def update(self, x):
        x += self.n

        self.tree[x] += 1

        x = x//2 if not x % 2 else (x - 1)//2

        while x > 0:
            self.tree[x] = self.tree[2 * x] + self.tree[2 * x + 1]
            x = x//2 if not x % 2 else (x - 1)//2

    def query(self, l, r):
        l += self.n
        r += self.n

        extra = 0

        while l < r:
            if l % 2:
                extra += self.tree[l]
                l = (l + 1)//2
            else:
                l //= 2

            if not r % 2:
                extra += self.tree[r]
                r = (r - 2)//2

            else:
                r = (r - 1)//2

        extra += self.tree[l] if l == r else 0

        return extra

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # segment tree
        # since the numbers are too large to create a segment tree by their values,
        # we create a segment tree by indices. We first sort the nums and assign them
        # indices based on their places in the sorted array
        # then for each num, we perform binary search to find the indices of 
        # lower - num and upper - num, then we query our segment tree for that range
        
        sorted_nums = sorted(nums)
        offset_indices = {}
        for ind, num in enumerate(sorted_nums):
            if num not in offset_indices:
                offset_indices[num] = ind

        tree = SegmentTree(len(nums) + 1)

        res = 0

        for num in nums:
            off_ind = offset_indices[num]

            left = lower - num
            left_ind = bisect.bisect_left(sorted_nums, left)

            right = upper - num
            right_ind = bisect.bisect_right(sorted_nums, right) - 1

            if left_ind <= right_ind:
                res += tree.query(left_ind, right_ind)

            tree.update(off_ind)

        return res

        


# Solution 3

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        def merge(left, right):
            nonlocal res
            
            for lnum in left:
                rnum1 = lower - lnum
                rnum2 = upper - lnum

                lbound = bisect.bisect_left(right, rnum1)
                rbound = bisect.bisect_right(right, rnum2)
                res += max(0, rbound - lbound)

            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr)//2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)

        mergeSort(nums)

        return res


