class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def wave(num):
            num = str(num)

            count = 0

            for i in range(1, len(num) - 1):
                if num[i-1] > num[i] < num[i + 1]:
                    count += 1

                if num[i - 1] < num[i] > num[i + 1]:
                    count += 1

            return count


        return sum(wave(num) for num in range(num1, num2 + 1))
        
