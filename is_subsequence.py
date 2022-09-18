#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
#of the characters without disturbing the relative positions of the remaining characters. 
#Input: s = "abc", t = "ahbgdc"
#Output: true

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                j=t.index(i)
                t=t[j+1:]
            else:
                return False
        return True