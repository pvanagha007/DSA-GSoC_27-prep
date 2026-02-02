class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Initialize an empty dictionary to store the last seen index of each element
        a={}
        #idx, value is for iterating thru nums
        #enumerate gives both index and value
        for idx,val in enumerate(nums):                       
            if val in a and idx-a[val]<=k:
                return True
            a[val]=idx
        return False

    #time complexity: O(n)
    #space complexity: O(n)