class Solution:
    def compressedString(self, word: str) -> str:
        # sliding window
        def add(letter, times):
            temp = ""
            if times <= 9:
                temp += str(times) + letter

            else:
                nine = times//9
                for _ in range(nine):
                    temp += str(9) + letter
                
                if times % 9:
                    temp += str(times % 9) + letter

            return temp

        comp = ""
        

        l = 0
        n = len(word)
        for r in range(n):
            if word[r] != word[l]:
                letter = word[l]
                pre = r - l
                comp += add(letter, pre)
                l = r

        last = n - l
        letter = word[-1]
        comp += add(letter, last)


        return comp


        
