class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # group transactions by name then by time such that
        # group[name][time] = set containing all cities that had have the same name and time

        res = []
       
        n = len(transactions)

        group = defaultdict(lambda : defaultdict(set))

        # grouping
        for i in range(n):
            name, time, amount, city = transactions[i].split(",")
            time = int(time)
            amount = int(amount)
            group[name][time].add(city)

        for i in range(n):
            name, time, amount, city = transactions[i].split(",")
            time = int(time)
            amount = int(amount)

            if amount > 1000:
                res.append(transactions[i])
                continue

            # look back and forward 60 minutes from time to see if there were any such trans
            for t in range(time - 60, time + 61):
                if t not in group[name]:
                    continue

                if t == time:
                    # this city isn't the only one which had the same name and time
                    if len(group[name][t]) > 1:
                        res.append(transactions[i])
                        break

                else:
                    # if there were multiple cities or there was only one city and it wasnt
                    # the current city we are checking
                    if (
                        len(group[name][t]) > 1 
                        or (len(group[name][t]) == 1 and city not in group[name][t])
                        ):

                        res.append(transactions[i])
                        break

    

        return res
        
