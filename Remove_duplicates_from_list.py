class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            count = nums.count(i)
            if count > 1:
                j = 1
                while j < count :
                    nums.remove(i)
                    j += 1
