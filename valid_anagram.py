#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1=[i for i in s]
        list2=[j for j in t]
        list1.sort()
        list2.sort()
        if list1==list2:
            return True 
        return False