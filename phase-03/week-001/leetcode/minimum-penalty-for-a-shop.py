class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n, penalties = len(customers), [] # an array to store penalties of each hour
        # the suffix array to hold suffix occurences of Y, and a var to count suffix
        suffY, suff = [0 for i in range(n)], 0 
        #populating the suffix array suffY
        for i in reversed(range(n)):
            if customers[i] == 'Y':
                suff += 1
            suffY[i] = suff

        preN = 0 #variable to store prefix occurences of N
        for i,x in enumerate(customers): # populating the penalties array
            curr = suffY[i] + preN
            penalties.append(curr)
            if x == 'N':
                preN += 1

        penalties.append(preN) # accounting for the hour(s) after the last hour

        hour = [0,penalties[0]] # to find the minimum penalty and store it with its hour
        for i,x in enumerate(penalties):
            if x < hour[-1]:
                hour = [i,x]

        return hour[0]

            

            
                
        