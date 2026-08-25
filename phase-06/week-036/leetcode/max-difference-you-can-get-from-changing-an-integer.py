class Solution:
    def maxDiff(self, num: int) -> int:
        res = 0


        maxx = minn = num

        for a in range(10):
            for b in range(a, 10):
                list_num_max = list(str(num))
                list_num_min = list(str(num))



                for i in range(len(list_num_max)):
                    
                    if int(list_num_max[i]) == a:
                        list_num_max[i] = str(b)

                for i in range(len(list_num_min)):

                    if int(list_num_min[i]) == b:
                        list_num_min[i] = str(a)

                curr_max = int("".join(list_num_max))
                if curr_max != 0 and list_num_max[0] != '0':
                    maxx = max(maxx, curr_max)

                curr_min = int("".join(list_num_min))
                if curr_min != 0 and list_num_min[0] != '0':
                    minn = min(minn, curr_min)

        return maxx - minn

            


        
        
