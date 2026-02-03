#using my own code
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        #sorting both strings
        a=sorted(s)
        b=sorted(t)

        #counting frequency of each character in string a
        counter=1
        count={}
        curr=a[0]
        for ch in a[1:]:
            if ch== curr:
                counter+=1
            else:
                count[curr]=counter
                curr=ch
                counter=1
        count[curr]=counter


        #counting frequency of each character in string b
        counter2=1
        count2={}
        curr2=b[0]
        for ch in b[1:]:
            if ch== curr2:
                counter2+=1
            else:
                count2[curr2]=counter2
                curr2=ch
                counter2=1
        count2[curr2]=counter2


        #comparing both frequency dictionaries
        for key in count2:
            if key not in count or count2[key] != count[key]:
                return False
        return True

