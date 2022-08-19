class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Stack:
    def __init__(self):
        self.start=None
        
    def push(self,data):
        if self.start==None:
            self.start=Node(data)
        else:
            temp=self.start
            self.start=Node(data)
            self.start.next=temp

    def pop(self):
        if self.start==None:
            return "stack underflow"
        else:
            popped=self.start.data
            self.start=self.start.next
            return popped
    def is_empty(self):
        if self.start==None:
            return True
        else:
            return False

    def peek(self):
        if self.start:
            return self.start.data

    def display(self):
        temp=self.start
        if self.start==None:
            return "empty stack"
        else:
            while temp!=None:
                print(temp.data)
                temp=temp.next

