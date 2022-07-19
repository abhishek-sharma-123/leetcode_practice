#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
#it reads the same forward and backward. 
#Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.





class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanums = [
                    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
                    "t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"
                    ]
        list1 = [i.lower() for i in s if i.lower() in alphanums]
        list2 = list1[::-1]
        if list1 == list2 :
            return True
        return False
        