#Given an array nums containing n distinct numbers in the range [0, n],
#return the only number in the range that is missing from the array.

 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        list1=[i*0 for i in range(len(nums)+1)]
        for i in nums:
            list1[i]=1
        for j in range(len(list1)):
            if list1[j]==0:
                return j
        return 