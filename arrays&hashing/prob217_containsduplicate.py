class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Initialize an empty set to store unique elements from the array.
        hashset = set()             
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
    
    #time complexity: O(n) because we are iterating through the array once, and each lookup and insertion operation in the set takes O(1) time on average.
    #space complexity: O(n) in the worst case, if all elements in the array are unique, we will store all n elements in the set.