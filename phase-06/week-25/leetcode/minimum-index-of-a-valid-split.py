class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # counting + sets 
        # instantiate two arrays with empty sets, one array for iterating left to right
        # and the other for iterating right to left
        # while iterating keep track of the count of each element seen, and for each 
        # index, store the in the set at that index the elements whose frequency is
        # more than half of the subarray iterated so far. Do this for both direction.
        # a valid index is an index whose set in the left-right array and the set at
        # index + 1 of the right-to-left array have a non-empty intersection

        n = len(nums)
        left = [set() for _ in range(n)]
        count = Counter()

        for i in range(n):
            x = nums[i]
            count[x] += 1
            # if it occurs more than half of the subarray, store it in the set at left[i]
            if count[x] > (i + 1)//2:
                left[i].add(x)

            # we also need to consider previous dominant elements, so check the set 
            # immediately before it too
            if i > 0:
                prev = left[i - 1]
                for x in prev:
                    if count[x] > (i + 1)//2:
                        left[i].add(x)



        right = [set() for _ in range(n)]
        count = Counter()

        for i in range(n -1, -1, -1):
            x = nums[i]
            count[x] += 1
            if count[x] > (n - i)//2:
                right[i].add(x)

            if i < n-1:
                nxt = right[i + 1]
                for x in nxt:
                    if count[x] > (n - i)//2:
                        right[i].add(x)


        for i in range(n - 1):
            if left[i] and right[i] and left[i].intersection(right[i + 1]):
                return i

        return -1


