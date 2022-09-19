#Given a string s which consists of lowercase or uppercase letters, 
#return the length of the longest palindrome that can be built with those letters.
#Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#Input: s = "abccccdd"
#Output: 7


class Solution:
    def longestPalindrome(self, s: str) -> int:
        length=0
        singles=0
        H=[i*0 for i in range(65,123)]
        for i in s:
            H[ord(i)-65]+=1
        for j in H:
            if j%2==0:
                length+=j
            else:
                length+=j-1
                singles+=1
        if singles==0:
            return length
        else:
            return length+1