class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # bit 
        # for each index i, compute the the ORs of all subarrays that end at index i
        # by ORing arr[i] with every possible OR of any subarray that ended at index i-1.
        # As we iterate, we store ever arr[i] as an OR value itself so that we can also
        # compute the ORs of subbarays that start at index i and end somewhere (i + 1, n)
        
        prev_ORs = set()
        
        ans = set()
        
        for x in arr:
            
            curr_ORs = {x}

            for y in prev_ORs:
                curr_ORs.add(y | x)
            
            ans.update(curr_ORs)
            
            prev_ORs = curr_ORs
        
        return len(ans)
