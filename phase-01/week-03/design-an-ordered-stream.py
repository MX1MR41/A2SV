class OrderedStream:

    def __init__(self, n):
        self.stream = [None] * n
        self.pointer = 0

    def insert(self, id_key, value):
        id_key -= 1
        self.stream[id_key] = value

        if self.pointer < id_key:
            return []
        else:
            while self.pointer < len(self.stream) and self.stream[self.pointer] is not None:
                self.pointer += 1
            return self.stream[id_key:self.pointer]

