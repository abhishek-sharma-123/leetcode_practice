#Given the head of a linked list and an integer val, 
#remove all the nodes of the linked list that has Node.val == val, and return the new head.


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        list1=[]
        temp=head
        if head==None:
            return head
        while temp!=None:
            list1.append(temp.val)
            temp=temp.next
        c=list1.count(val)
        for i in range(c):
            list1.remove(val)
        temp=head
        p=head
        for i in list1:
            temp.val=i
            p=temp
            temp=temp.next
        if len(list1)==0:
            head=None
        p.next=None
        return head