class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # binary search
        # store the indices where for each index, nums[index] has same parity as nums[index + 1]
        # then for every query, do a binary search to see if any value in between the query 
        # endpoints exists
        
        invalids = []
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                invalids.append(i)

        def search(start, end):
            l, r = 0, len(invalids) - 1
            while l <= r:
                mid = (l + r)//2
                if start <= invalids[mid] < end:
                    return True

                if invalids[mid] < start:
                    l = mid + 1
                else:
                    r = mid - 1

            return False

        
        res = []

        for start, end in queries:
            if start == end:
                res.append(True)
                continue
            if search(start, end):
                res.append(False)
            else:
                res.append(True)


        return res


        
