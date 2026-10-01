class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        for c in s:
            if c.isalnum():
                new_s+=c.lower()
        length=len(new_s)
        for i in range(length//2):
            if new_s[i]!=new_s[length-(i+1)]:
                return False
        return True
            
            

        