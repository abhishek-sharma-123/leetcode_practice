class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        temp=head
        while temp!=None:
            list1.append(temp.val)
            temp=temp.next
        list2=list1[::-1]
        temp=head
        for i in list2:
            temp.val=i
            temp=temp.next
        return head
        