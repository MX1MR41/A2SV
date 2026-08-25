class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # dp + prefix sum + sweep line
        # for each day, we need to keep track of the number of people who can share the secret
        # and the number of people who know the secret. When a person shares a secret, 
        # the number of people who know the secret from today upto today + forget increase by 1,
        # and the number of people who can share it from today + delay upto today + forget also
        # increases by 1. So to perform range update easily, we use two prefix sum arrays an two
        # running sum variable that will keep adding the values seen so far and update the 
        # prefix sum values in a sweep line fashion, basically, an online prefix sum.

        knows_psum = [0] * (n + 1) # knows_psum[i] -> number of people who know on day i
        shares_psum = [0] * (n + 1) # shares_psum[i] -> number of people who can share on day i

        knows_rsum = 1 # number of people who know on the current day
        shares_rsum = 0 # number of people who can share on the current day
        
        # initialization due to the person who got to know the secret on day 1
        knows_psum[1] = 1

        # can start sharing on day 1 + delay
        if 1 + delay <= n:
            shares_psum[1 + delay] = 1

        # will forget and stop sharing on day 1 + forget
        if 1 + forget <= n:
            knows_psum[1 + forget] = -1
            shares_psum[1 + forget] = -1

        # start from day 2
        for i in range(2, n + 1):
            
            #  update the running sum then the prefix sum respectively
            shares_rsum += shares_psum[i]
            shares_psum[i] = shares_rsum

            # i.e. there are people who can share a secret today
            # if there are shares_sum people, each will share to 1 person
            # so a total of new shares_sum people will know the secret 
            # starting from today upto today + forget
            # and they can start sharing on today + delay
            if shares_rsum > 0:
                knows_psum[i] += shares_rsum
                if i + delay <= n:
                    shares_psum[i + delay] += shares_rsum

                if i + forget <= n:
                    knows_psum[i + forget] += -shares_rsum
                    shares_psum[i + forget] += -shares_rsum

            knows_rsum += knows_psum[i]
            knows_psum[i] = knows_rsum

        return knows_psum[n] % (10**9 + 7)
