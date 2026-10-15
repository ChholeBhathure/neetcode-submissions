class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=left+1
        res=set()
        max_char=0
        for right in range(len(s)):
            while s[right] in res:
                res.remove(s[left])
                left=left+1
                
            res.add(s[right])
            max_char=max(max_char,len(res))
        return max_char

            


        