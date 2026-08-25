class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        hash = {str(i): i for i in range(10)}
        num_1, num_2 = 0, 0
        len_1, len_2 = len(num1), len(num2)
        
        for i in range(len(num1)):
            num_1 += hash[num1[i]] * (10 ** (len_1 - 1))
            len_1 -= 1

        for i in range(len(num2)):
            num_2 += hash[num2[i]] * (10 ** (len_2 - 1))
            len_2 -= 1

        return(str(int(num_1 * num_2)))


        