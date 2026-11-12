class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        MapS = {}
        MapT = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in MapS:
                MapS[s[i]] = 0
            else:
                MapS[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in MapT:
                MapT[t[i]] = 0
            else:
                MapT[t[i]] += 1
    
        return MapT == MapS
        

            
        