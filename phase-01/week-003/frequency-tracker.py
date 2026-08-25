from collections import defaultdict

class FrequencyTracker:
    def __init__(self):
        self.count = defaultdict(int)
        self.freq = defaultdict(set)

    def add(self, number):
        prev = self.count[number]

        if number in self.freq[prev]:
            self.freq[self.count[number]].remove(number)

        self.count[number] += 1
        new = prev + 1
        self.freq[new].add(number)

    def deleteOne(self, number):
        if number in self.freq[self.count[number]]:
            self.freq[self.count[number]].remove(number)

        if self.count[number]:
            self.count[number] -= 1
            if self.count[number] == 0:
                del self.count[number]
            else:
                new = self.count[number]
                self.freq[new].add(number)

    def hasFrequency(self, frequency):
        return bool(self.freq[frequency])
