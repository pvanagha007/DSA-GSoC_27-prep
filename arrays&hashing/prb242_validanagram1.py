#using built in library Counter, which is a subclass of dict that helps count hashable objects. It counts the number of occurrences of each element in the input and stores it as a dictionary where the keys are the elements and the values are their counts.
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s)==Counter(t):
            return True
        else:
            return False