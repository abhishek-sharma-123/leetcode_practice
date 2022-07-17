class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        list1 = [a[i] for i in range(len(a))]
        list2 = list1[::-1]
        if list1 == list2:
            return True 
        return False