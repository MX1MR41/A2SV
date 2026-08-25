class Solution:
    def longestPalindrome(self, s: str) -> int:
        # when forming a palindrome, we are allowed with one letter of odd occurence and 
        # infinite letters of even occurences
        # in case we meet a second or third .. odd letter, we add its ocurrence - 1 (to make it even)
        seen_odd = False 
        res = 0
        cnt = Counter(s)

        for letter in cnt:
            count = cnt[letter]
            if not count % 2:
                res += count

            elif count % 2:
                if not seen_odd:
                    res += count
                    seen_odd = True
                else:
                    res += count - 1 

            
        return res
        