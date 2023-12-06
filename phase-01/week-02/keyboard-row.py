class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_set =  set("qwertyuiop")
        second_set =  set("asdfghjkl")
        third_set =  set("zxcvbnm")
        res = []

        for i in words:
            sub = set(i.lower())
            if sub.issubset(first_set) or sub.issubset(second_set) or sub.issubset(third_set):
                res.append(i)

        return res


        