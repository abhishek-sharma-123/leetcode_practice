class MyStack:

    def __init__(self):
        self.queue=[]

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        item=self.queue.pop(-1)
        return item

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if self.queue==[]:
            return True
        return False
