from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Create a dictionary to store groups
        anagrams = defaultdict(list)  # key: frequency tuple, value: list of words
        
        # Step 2: Process each word
        for word in strs:
            # Step 2a: Create a 26-letter count
            count = [0] * 26  # for 'a' to 'z'
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            # Step 2b: Convert count list to tuple (lists can't be dict keys since they're mutable)
            key = tuple(count)
            
            # Step 2c: Add the original word to the group
            anagrams[key].append(word)
        
        # Step 3: Return all the groups as a list of lists
        return list(anagrams.values())
    

'''Complexity

Time: O(N * K), where N = number of strings, K = max length of a string

We just loop through each character (no sorting)

Space: O(N * K), for storing the groups and keys'''
