#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.


# Method-1 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        i=0
        j=0
        while i < len(nums) and j < len(nums):
            if nums[i] == 0:
                if nums[j] == 0:
                    j+=1
                else:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    i += 1
                    j += 1
            else:
                i+=1
                j+=1


#Method-2
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a = nums.count(0)
        for i in range(a):
            nums.remove(0)
        for j in range(a):
            nums.append(0)