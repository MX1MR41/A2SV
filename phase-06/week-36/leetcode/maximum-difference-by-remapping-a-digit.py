class Solution:
    def minMaxDifference(self, num: int) -> int:
        res = 0


        maxx = minn = num

        for a in range(10):
            for b in range(a + 1, 10):
                list_num_max = list(str(num))
                list_num_min = list(str(num))



                for i in range(len(list_num_max)):
                    
                    if int(list_num_max[i]) == a:
                        list_num_max[i] = str(b)

                for i in range(len(list_num_min)):

                    if int(list_num_min[i]) == b:
                        list_num_min[i] = str(a)

                maxx = max(maxx, int("".join(list_num_max)))
                minn = min(minn, int("".join(list_num_min)))


        return maxx - minn

            


        
