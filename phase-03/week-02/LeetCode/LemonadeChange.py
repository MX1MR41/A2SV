class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10:
                if fives < 1:
                    return False
                tens += 1
                fives -= 1
            else:
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False

        return True