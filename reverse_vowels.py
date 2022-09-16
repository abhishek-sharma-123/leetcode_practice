#Given a string s, reverse only all the vowels in the string and return it.
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

class Solution:
    def reverseVowels(self, s: str) -> str:
        list1=[i for i in s]
        vowel=['a','e','i','o','u','A','E','I','O','U']
        list2=[j for j in s if j in vowel]
        list2=list2[::-1]
        k=0
        for i in range(len(list1)):
            if list1[i] in vowel:
                list1[i]=list2[k]
                k+=1
        return "".join(list1)