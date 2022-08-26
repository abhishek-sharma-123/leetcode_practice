#Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=head
        list1=[]
        while temp!=None:
            list1.append(temp.val)
            temp=temp.next
        if list1==list1[::-1]:
            return True
        return False