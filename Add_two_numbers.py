#You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in reverse order, and each of their nodes contains a single digit.
#Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#for example:
# Input:
    # l1= 2 --> 4 --> 3
    # l2= 5 --> 6 --> 4
# Output:
    # 7 --> 0 --> 8
#explaination 342 + 465 = 807





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        list2=[]
        temp1=l1
        temp2=l2
        while temp1!=None:
            list1.append(str(temp1.val))
            temp1=temp1.next
        while temp2!=None:
            list2.append(str(temp2.val))
            temp2=temp2.next
        list1.reverse()
        list2.reverse()        
        len1=len(list1)
        len2=len(list2)        
        v1=int("".join(list1))
        v2=int("".join(list2))
        v3=v1+v2
        v3=str(v3)
        list3=[int(i) for i in v3]
        list3=list3[::-1]
        start=ListNode(list3[0])
        first=start
        for i in range(1,len(list3)):
            new_node=ListNode(list3[i])
            start.next=new_node
            start=start.next
        return first