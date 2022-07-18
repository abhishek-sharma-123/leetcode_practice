class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if len(nums) > 1:
                for i in range(len(nums)-1):
                    if nums[i] < target and nums[i+1] > target :
                        return i+1
                if nums[-1] < target:
                    return len(nums) 
                if nums[0] > target:
                    return 0                
            elif len(nums) == 0:
                return 0
            else:
                if nums[0] > target:
                    return 0
                else:
                    return 1