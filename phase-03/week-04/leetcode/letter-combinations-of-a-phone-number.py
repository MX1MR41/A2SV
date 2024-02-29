class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "1":[], "2":["a","b","c"], "3":["d","e","f"],
            "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"],
            "7":["p","q","r","s"], "8":["t","u","v"], "9": ["w","x","y","z"]
        }

        res = []
        
        def combine(ind, s):
            

            if ind == len(digits):
                if not len(digits):
                    return
                res.append(s)
                return

            curr = d[digits[ind]]
            for i in curr:
                s += i
                combine(ind + 1, s)
                s = s[:-1]

        combine(0,"")
        return res
