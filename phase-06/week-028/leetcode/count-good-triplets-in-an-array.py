# Solution 1 

class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)

    def update(self, x):
        x += self.n

        self.tree[x] += 1

        x = x//2 if x % 2 == 0 else (x - 1)//2

        while x > 0:
            self.tree[x] = self.tree[2*x] + self.tree[2*x + 1]
            x = x//2 if x % 2 == 0 else (x - 1)//2

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

            if r % 2 == 0:
                extra += self.tree[r]
                r = (r - 2)//2
            else:
                r = (r - 1)//2

        extra += self.tree[l] if l == r else 0

        return extra



class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # segment tree
        # store the indices of the numbers from nums1 in inds1
        # while iterating on nums2, get the index of each num from inds1
        # query how many nums with indices < inds1[num] have been seen so far
        # do this from both the left and right, then for every num assume it is the 
        # middle num and do left[x] * right[x] because that is the total number of 
        # unique combinations that can be formed with x in the middle

        inds1 = {num: ind for ind, num in enumerate(nums1)}

        prev = defaultdict(int)

        n = len(nums1)

        tree = SegmentTree(n + 1)

        for num in nums2:
            ind = inds1[num]

            count_prev = tree.query(0, ind - 1) if ind != 0 else 0
            prev[num] = count_prev

            tree.update(ind)


        tree = SegmentTree(n + 1)
        nxt = defaultdict(int)

        for num in nums2[::-1]:
            ind = inds1[num]

            nxt_count = tree.query(ind + 1, n)
            nxt[num] = nxt_count

            tree.update(ind)

        res = 0
        for i in range(n):
            res += prev[i] * nxt[i]

        return res




# Solution 2

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # merge sort
        # for every num x, count the number of elements that come before it in both
        # arrays and store in prev dictionary, count the number of elements that come
        # after it in both arrays in nxt dictionary, then compute the good triplets
        # as prev[x] * nxt[x] by considering x as the middle element
        # use merge sort algorithm to compare and count in parallel

        def merge(left, right, inds, prev, nxt):
            
            # counting process
            # since we know that left and right are already independently sorted arrays
            # we can use that property to quickly calculate how many numbers in right 
            # occur after num for every num in left, AND how many number in left occur
            # before num for every num in right. The indices themselves tell us how
            # many steps we've moved and consequently how many nums have been counted

            i = j = 0

            while j < len(right):
                # try to find the last number in left that occurs before right[j]
                # pointer i will stops just past that last valid number
                while i < len(left) and inds[left[i]] < inds[right[j]]:
                    # since left[i] occurs before right[j], that means it also occurs
                    # before all nums in right starting from j upto the end of right
                    nxt[left[i]] += len(right) - j

                    i += 1

                # i will stop at the first number in left that occurs after right[j],
                # hence i numbers occur before right[j]
                prev[right[j]] += i
                j += 1



            # merging process
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if inds[left[i]] < inds[right[j]]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged

        def mergeSort(arr, inds, prev, nxt):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = mergeSort(arr[:mid], inds, prev, nxt)
            right = mergeSort(arr[mid:], inds, prev, nxt)

            return merge(left, right, inds, prev, nxt)

        inds1 = {num: ind for ind, num in enumerate(nums1)}
        prev = defaultdict(int)
        nxt = defaultdict(int)

        mergeSort(nums2, inds1, prev, nxt)

        res = 0

        n = len(nums1)

        for i in range(n):
            res += prev[i] * nxt[i]

        return res

