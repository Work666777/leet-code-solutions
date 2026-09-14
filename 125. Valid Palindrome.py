class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for l in s:
            if l.isalnum():
                newstr += l.lower()
        if newstr == newstr[::-1]:
            return True
        else: return False