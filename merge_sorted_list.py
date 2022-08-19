class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p=list1
        q=list2
        start=None
        end=None
        if p!=None and q!=None:
            if p.val<q.val:
                start=p
                end=p
                p=p.next
            else:
                start=q
                end=q
                q=q.next
        else:
            if p:
                return p
            elif q:
                return q
            else:
                return p
        while p!=None and q!=None:
            if p.val<q.val:
                end.next=p
                end=end.next
                p=p.next
            else:
                end.next=q
                end=end.next
                q=q.next
        if p:
            end.next=p
        elif q:
            end.next=q
        return start