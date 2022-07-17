class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 =dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)
        list1 = ['I','V','X','L','C','D','M']
        num = 0
        i = 0
        while i < len(s):
            j = i + 1
            if i < len(s)-1:
                if list1.index(s[i]) >= list1.index(s[j]):
                    num += dict1[s[i]]
                    i += 1
                else:
                    num += dict1[s[j]] - dict1[s[i]]
                    i += 2
            else:
                num += dict1[s[i]]
                i +=1
        return num