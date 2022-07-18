class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list1 = [str(i) for i in digits]
        num = ""
        num = int(num.join(list1))
        num = str(num + 1)
        array = [int(i) for i in num]
        return array