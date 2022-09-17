#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

#Each letter in magazine can only be used once in ransomNote.
#Input: ransomNote = "a", magazine = "b"
#Output: false
 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=[i for i in ransomNote]
        m=[j for j in magazine]
        for k in r:
            if k in m:
                m.remove(k)
            else:
                return False
        return True