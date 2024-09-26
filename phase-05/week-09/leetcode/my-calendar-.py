class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:

            if start < e and end > s:
                return False

        self.calendar.append((start, end))
        return True
