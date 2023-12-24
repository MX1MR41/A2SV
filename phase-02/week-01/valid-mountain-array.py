class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n, cnt = len(arr), 0
        
        if n <= 2:
            return False

        flag1, flag2 = False, False

        i = 1

        while i < n:
            if arr[i] == arr[i-1]:
                return False

            if arr[i] < arr[i-1]:
                if not flag2:
                    flag2 = True
                elif i == n - 1 and not flag1:
                    return False

            if arr[i] > arr[i-1]:
                if not flag1:
                    flag1 = True
                if flag1 and flag2:
                    return False
                if i == n - 1 and not flag2:
                    return False

            i += 1

        return True
