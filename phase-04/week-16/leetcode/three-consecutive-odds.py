class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        def isOdd(temp):
            for i in temp:
                if not i % 2:
                    return False
            return True

        n = len(arr)
        if n < 3:
            return False

        curr = arr[:3]
        if isOdd(curr):
            return True
        
        for j in range(3,n):
            curr.pop(0)
            curr.append(arr[j])

            if isOdd(curr):
                return True

        return False
        
