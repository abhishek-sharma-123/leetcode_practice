#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

#You must implement a solution with a linear runtime complexity and use only constant extra space.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0 
        while i < len(nums):
            if nums.count(nums[i]) == 1:
                break
            i+=1
        return nums[i]
        