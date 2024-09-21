class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # keep adding zeros until you can't
        # keep cutting off last digits until it's a valid number
        ans = []
        curr = 1
        
        for _ in range(n):
            ans.append(curr)

            if curr * 10 <= n:
                curr *= 10 

            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10 

                curr += 1 

        return ans
