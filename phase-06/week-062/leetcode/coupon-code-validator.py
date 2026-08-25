class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_business = set(["electronics", "grocery", "pharmacy", "restaurant"])

        def valid_code(c):
            if not c:
                return False

            for i in c:
                if not i.isalnum() and i != "_":
                    return False

            return True

        res = []
        for i in range(len(code)):
            c = code[i]
            b = businessLine[i]
            a = isActive[i]
            if a and b in valid_business and valid_code(c):
                res.append((b, c))

        res.sort()
 

        return [i[1] for i in res]
