class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)

        steps = 0
        num = 0
        move = 1

        while True:
            num += move
            steps += 1
            move += 1


            # if the diff is even, then it indicates that we can modify the steps we took
            # by flipping one sign from + to -. Hence incuring a total loss of twice that
            # number whose sign we flipped
            if num >= target and not (num - target) % 2:
                return steps

                

        
