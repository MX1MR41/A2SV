class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        arr2 = sorted(arr)
        if arr == arr2: # no need to pancake sort
            return []

        n, ans = len(arr), []

        for i in reversed(range(n)):
            a = arr2.pop() # get the biggest element of this iteration
            b = arr.index(a) # get the index of said biggest number in arr
            if b != i: # if the number isnt in its rightful place
        
                l, r = 0, b # reverse the subarr till that element
                while l < r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1

                l, r = 0, i # reverse the subarr till this iteration's end
                while l < r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
                ans.append(b+1) 
                ans.append(i+1)

        return ans
