class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = Node(homepage)
        self.last = self.home
        self.curr = self.home
        

    def visit(self, url: str) -> None:
        new = Node(url)
        if self.last != self.curr:
            new.prev = self.curr
            self.curr.next = new
            self.curr = self.curr.next
            self.last = self.curr
        else:
            new.prev = self.last
            self.last.next = new
            self.last = self.last.next
            self.curr = self.last


        

    def back(self, steps: int) -> str:
        dummy = self.curr
        while dummy.prev and steps:
            dummy = dummy.prev
            steps -= 1

        self.curr = dummy
        return dummy.val

        
        

    def forward(self, steps: int) -> str:

        dummy = self.curr
        while dummy.next and steps:
            dummy = dummy.next
            steps -= 1
        
        self.curr = dummy
        return dummy.val
        


