class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        cnt1 = Counter(target)
        cnt2 = Counter(arr)
        for num in cnt1:
            if cnt1[num] != cnt2[num]: return False

        return True
        
