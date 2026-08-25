class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # dp + math
        # assume there are no plants, so instead of SSPPSS it would be SSSS
        # in which case there is only one was of divison => SS|SS
        # if SSSSSS => SS|SS|SS, so basically grouping the S's by twos
        # if one plant was added in the middle of SSSS => SSPSS,
        # there would be two ways => SS|PSS, SSP|SS
        # if two plants were added SSPPSS => SS|PPSS, SSP|PSS, SSPP|SS
        # so for a boundary between a grouping of two S's the number of ways that 
        # this boundary could be divided is going to be the distance between the
        # last S of this group and the first S of the next group
        # then we just multiply the ways of each boundary to get the total 
        


        res = 1

        count = -1
        last = -1

        for i in range(len(corridor)):
            if corridor[i] == "S":
                count += 1

                if count % 2 == 0 and last != -1:
                    
                    dist = i - last
                    res = (res * dist) % 1000000007

                last = i

        if (count + 1) % 2 == 1 or (count + 1) == 0:
            return 0

        return res 

        
