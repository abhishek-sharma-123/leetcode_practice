#Given an integer array nums, return the third distinct maximum number in this array. 
#If the third maximum does not exist, return the maximum number.
#Input: nums = [3,2,1]
#Output: 1


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        i=0
        list1=[]
        nums=set(nums)
        nums=list(nums)
        if len(nums)<3:
            return max(nums)
        nums.sort()
        return nums[-3]