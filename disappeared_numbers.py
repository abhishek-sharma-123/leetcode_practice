#Given an array nums of n integers where nums[i] is in the range [1, n], 
#return an array of all the integers in the range [1, n] that do not appear in nums.
#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [5,6]
 

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        H=[i*0 for i in range(1,n+1)]
        list1=[]
        for i in nums:
            H[i-1]+=1
        for i in range(len(H)):
            if H[i]==0:
                list1.append(i+1)
        return list1
        