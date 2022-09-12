#Given a linked list, swap every two adjacent nodes and return its head. 
#You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#Input: head = [1,2,3,4]
#Output: [2,1,4,3]

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return
        temp=head
        p=None
        q=None
        r=None
        while temp!=None:
            if temp.next:
                q=temp.next
                p=temp
                r=p.val
                p.val=q.val
                q.val=r
                temp=temp.next.next
            else:
                return head
        return head