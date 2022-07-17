class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        j = 0
        list1 = sorted(strs, key = len)
        if len(strs) > 1:
            while j < len(list1[0]):
                prefix = list1[0][j]
                for i in range(1, len(list1)):
                    if list1[i][j] == prefix:
                        if i == len(list1) - 1:
                            output = output + prefix
                            j += 1
                    else:
                        j+=len(list1[0]) 
                        break
        else:
            output = output + list1[0]
        return output
        