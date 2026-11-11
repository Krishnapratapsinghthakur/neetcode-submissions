class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        if len(s)!=len(t):
            return False
            
        s.sort()
        t.sort()
        for i in range(0,len(s)):
            if s[i]==t[i]:
                continue
            else:
                return False
        return True
    


        