#Write a function that reverses a string. The input string is given as an array of characters s.

#You must do this by modifying the input array in-place with O(1) extra memory.

 

class Solution:
    def reverseString(self, s: List[str]) -> None:

        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while j>i:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            i+=1
            j-=1
        return s
        