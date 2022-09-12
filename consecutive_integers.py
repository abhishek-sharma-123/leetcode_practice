#Given an integer num, return three consecutive integers (as a sorted array) that sum to num.
#If num cannot be expressed as the sum of three consecutive integers, return an empty array.
#Input: num = 33
#Output: [10,11,12]
 

class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        list1=[]
        if num%3==0:
            a=num//3
            list1.append(a-1)
            list1.append(a)
            list1.append(a+1)
            return list1
        return list1