class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = [i for i in nums if i < pivot]
        equal = [i for i in nums if i == pivot]
        more = [i for i in nums if i > pivot]

        return ( less + equal + more)
        