class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        nums = []

        if not (num - 3) % 3:
            n = ((num - 3) // 3)
            print(n)
            nums = [n , n + 1 , n + 2]
            
        return nums
        