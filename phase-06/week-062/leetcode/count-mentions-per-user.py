class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key = lambda x: [int(x[1]), -ord(x[0][0])])


        offline = defaultdict(lambda : float("-inf"))

        mentions = [0] * numberOfUsers

        for i in range(len(events)):

            if events[i][0] == "MESSAGE":

                if events[i][2] == "HERE":

                    timestamp = int(events[i][1])
                    for id in range(numberOfUsers):

                        if offline[id] <= timestamp:
                            mentions[id] += 1
                            del offline[id]


                    continue

                if events[i][2] == "ALL":
                    for id in range(numberOfUsers):
                        mentions[id] += 1

                    continue

    

                ids = [int(j[2:]) for j in events[i][2].split()]
                for id in ids:
                    mentions[id] += 1

                continue


            id = int(events[i][2])
            timestamp = int(events[i][1])
            offline[id] = timestamp + 60


        return mentions
        
