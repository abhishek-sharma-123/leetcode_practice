#Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.




class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        if p==None:
            return p
        else:
            if p.next!=None:
                q=p.next
            else:
                return p
        while q.next!=None:
            if q.val==p.val:
                q=q.next
            else:
                p.next=q
                p=q
                q=q.next
        if p.val==q.val:
            p.next=None
        else:
            p.next=q

        return head