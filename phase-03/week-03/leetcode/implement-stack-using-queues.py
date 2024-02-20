class MyStack:

    def __init__(self):
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        self.q2.appendleft(x)
        

    def pop(self) -> int:
        return self.q2.popleft()

        

    def top(self) -> int:
        return self.q2[0]
        

    def empty(self) -> bool:
        if not self.q2:
            return True
        return False
        

