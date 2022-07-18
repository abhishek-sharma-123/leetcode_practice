class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while i < len(nums):
            if nums[p] == val:
                nums.pop(p)
            else:
                i+=1