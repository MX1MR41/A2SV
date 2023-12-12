class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        n = 25/100*(len(arr))

        for i in count.keys():
            if count[i] > n:
                return i 
        