class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        d = {x - 96 : chr(x)  for x in range(97, 123) }
        # map to hold number to letter like 1:a, 2:b, 3:c...
        d[0] = 'z' # adding this to handle when there is a one back shift from 'a
        n = len(s)
        arr  = [0 for _ in range(n+1)]
        res = ""

        for start,end,shift in shifts: # range updates using the prefix sum method
            if not shift:
                arr[start] += -1
                arr[end+1] += 1
            else:
                arr[start] += 1
                arr[end+1] += -1

        psum = 0 #calculate the net operation for each element by index as prefix sum
        for i in range(n+1):
            psum += arr[i]
            arr[i] = psum

        for j in range(n):
            net = ord(s[j]) - 96 + arr[j] # -96 because the code handles a,b,c as 1,2,3
            res += d[net % 26]

        return res
        