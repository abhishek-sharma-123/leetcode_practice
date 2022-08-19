class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.start=None
    def insert_last(self,value):
        new_node=node(value)
        if self.start==None:
            self.start=new_node
        else:
            temp=self.start
            while temp.next != None:
                temp = temp.next
            temp.next=new_node
    def view(self):
        if self.start==None:
            print("empty")
        else:
            temp=self.start        
            while temp!=None:
                print(temp.data)
                temp = temp.next 
    def delete_first(self):
        if self.start==None:
            print("empty")           
        else:
            self.start=self.start.next

    def insert(self,value,index):
        new_node=node(value)
        temp = self.start
        if index>0:
            for i in range(index-1):
                temp=temp.next
            next_node=temp.next
            temp.next=new_node
            new_node.next=next_node
        else:
            self.start=new_node
            self.start.next=temp

    def count_nodes(self):
        ct = 0
        temp=self.start
        while temp!=None:
            ct+=1
            temp=temp.next
        return ct

    def sum(self):
        add=0
        temp=self.start
        while temp!=None:
            add+=temp.data
            temp=temp.next
        return add

    def maximum(self):
        if self.start!=None:
            temp=self.start
            maxx=temp.data
            while temp!=None:
                if temp.data>maxx:
                    maxx=temp.data
                temp=temp.next
            return maxx
        else:
            return 0

    def search(self,value):
        temp=self.start
        while temp!=None:
            if temp.data==value:
                return temp
            temp=temp.next
        return "Not in list"

    def delete(self,index):
        if index==0:
            self.start=self.start.next
        else:
            temp=self.start
            for i in range(index-1):
                temp=temp.next
            temp2=temp.next
            temp.next=temp2.next

    def is_sorted(self):
        if self.start==None:
            print("empty list")
        else:
            temp2=self.start
            temp=temp2.next
            while temp !=None:
                if temp2.data>temp.data:
                    return False
                    break
                else:
                    temp2=temp
                    temp=temp.next
            return True

    def concatenation(self,p,q):
        temp=p.start
        while temp.next!=None:
            temp=temp.next
        temp.next=q.start

    def merge(self,list1,list2):
        first=list1
        second=list2
        if first.data<second.data:
            third=list1.start
            last=list1.start
            first=first.next
            third.next=None
        else:
            third=list2.start
            last=list2.start
            second=second.next
            third.next=None
        while list1!=None and list2!=None:
            if first.data>second.data:
                last.next=second
                last=second
                second=second.next
                last.next=None
            else:
                last.next=first
                last=first
                first=first.next
                last.next=None
        if first!=None:
            last.next=first
        else:
            last.next=second
        return third




mylist = linked_list()
mylist.insert_last(10)
mylist.insert_last(20)
mylist.insert_last(30)
mylist.insert_last(40)
mylist.insert(25,2)

list2 = linked_list()
list2.insert_last(50)
list2.insert_last(60)
list2.insert_last(70)
mylist.merge(mylist,list2)
print("modified")
mylist.view()