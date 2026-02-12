#using neetcode solution watch the youtube video, same as mine but uses less variables, hence runtime and space is optimized
class Solution:
    #the usual class and function definition for leetcode problems, where we define a class named Solution and a method named isAnagram that takes two strings s and t as input and returns a boolean value indicating whether the two strings are anagrams of each other.
    def isAnagram(self, s: str, t: str) -> bool: 
        if len(s)!=len(t):
            return False
        countS={}
        countT={}

        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0) #if key doesn't exist, return 0
            countT[t[i]]=1+countT.get(t[i],0)
        
        for key in countS:
            if countS[key]!=countT.get(key,0): 
                return False
        return True

