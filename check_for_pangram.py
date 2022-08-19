#A pangram is a sentence where every letter of the English alphabet appears at least once.

#Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        list1 = [i for i in sentence]
        list2 =[
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'
        ,'t','u','v','w','x','y','z']
        list3 = [j for j in list2 if j in list1]
        if len(list3) == 26:
            return True
        return False