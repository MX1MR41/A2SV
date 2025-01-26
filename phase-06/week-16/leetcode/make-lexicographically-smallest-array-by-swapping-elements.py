class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # heap
        # if you can swap between number a and number b, then you can swap 
        # between number a and every number that can be swapped with b
        # so the problem has a unionfind structure, where we group numbers within
        # swappable proximity together, then assign them each appropiate indices,
        # i.e. the smallest num gets the smallest index of its groupmates
        # we can simulate the process with two heaps
        # at any moment, our heaps will contain nums and indices respectively 
        # that can be swapped. When we have got all groupmates together, we
        # can keep popping from both heaps to assign the smallest num to 
        # the smallest index
        
        def helper(numheap, indheap):
            while numheap:
                num = heappop(numheap)
                ind = heappop(indheap)
                nums[ind] = num


        arr = sorted([[num, ind] for ind, num in enumerate(nums)])

        n = len(nums)
        indheap, numheap = [arr[0][1]], [arr[0][0]]
        for i in range(1, n):
            num, ind = arr[i]
            if abs(num - arr[i - 1][0]) > limit:
                helper(numheap, indheap)

            heappush(numheap, num)
            heappush(indheap, ind)

        helper(numheap, indheap)

            
        
        return nums

        
