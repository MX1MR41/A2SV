class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        arr = [True]
        n = len(derived)
        for i in range(1, n):
            xor = derived[i - 1]
            if xor:
                arr.append(not arr[-1])
            else:
                arr.append(arr[-1])

        xor = derived[-1]
        if xor and arr[0] != arr[-1]:
            return True
        if not xor and arr[0] == arr[-1]:
            return True


        return False

        
