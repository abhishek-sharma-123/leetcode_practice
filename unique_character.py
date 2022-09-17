#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

#Input: s = "leetcode"
#Output: 0

class Solution:
    def firstUniqChar(self, s: str) -> int:
        list1=[]
        h=[i*0 for i in range(26)]
        for i in s:
            h[ord(i)-97]+=1
        for j in range(len(h)):
            if h[j]==1:
                list1.append(s.index(chr(j+97)))
        if list1==[]:
            return -1
        return min(list1)