import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        L, R = 0, len(s) - 1
        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return False
        return True
        
            