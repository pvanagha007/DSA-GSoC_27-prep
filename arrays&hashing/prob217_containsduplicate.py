class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Initialize an empty set to store unique elements
        hashset = set()             
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
    
    #time complexity: O(n)
    #space complexity: O(n)