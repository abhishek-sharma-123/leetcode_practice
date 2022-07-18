class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        list1 = []
    # loop for deleting spaces after the last letter of string
        while i >= 0:
            if s[i] == " ":
                i -= 1
            else:
                break
    # loop for detecting the space just before the last word
        while i >= 0:
            if s[i] == " ":
                break
            else :
                list1.append(s[i])
                i -=1
        return len(list1)
    
