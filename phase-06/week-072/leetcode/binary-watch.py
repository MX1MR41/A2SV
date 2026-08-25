class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # factorial
        # dfs

        res = set()

        def valid(hour, minute):

            if hour < 12 and minute < 60:
                return True, str(hour) + ':' + str('0' + str(minute))[-2:]
            else:
                return False, ''



        def fact(hour, minute):
            if hour.bit_count() + minute.bit_count() == turnedOn:
                val, time = valid(hour, minute)
                if val:
                    res.add(time)
                return 

            for i in range(4):
                if not hour & (1 << i):
                    new_hour = hour | (1 << i)

                    fact(new_hour, minute)

            for i in range(6):
                if not minute & (1 << i):
                    new_minute = minute | (1 << i)

                    fact(hour, new_minute)


        fact(0, 0)
        return list(res)


        
