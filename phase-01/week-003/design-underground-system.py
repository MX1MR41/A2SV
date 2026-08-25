class UndergroundSystem:

    def __init__(self):
        self.t = {} 
        self.c = {}  

    def checkIn(self, cid, st, t):
        self.c[cid] = (st, t)

    def checkOut(self, cid, et, t):
        st, ti = self.c.pop(cid)
        route = (st, et)
        dur = t - ti

        if route in self.t:
            tot, cnt = self.t[route]
            self.t[route] = (tot + dur, cnt + 1)
        else:
            self.t[route] = (dur, 1)

    def getAverageTime(self, st, et):
        route = (st, et)
        tot, cnt = self.t[route]
        return tot / cnt if cnt else 0
