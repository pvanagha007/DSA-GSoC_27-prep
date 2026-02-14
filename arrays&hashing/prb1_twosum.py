#one pass solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}

        for idx,val in enumerate(nums):
            diff=target-val
            if diff in a:
                return[a[diff],idx]
            a[val]=idx
       

#time complexity : O(n)
#space complexity: O(n)