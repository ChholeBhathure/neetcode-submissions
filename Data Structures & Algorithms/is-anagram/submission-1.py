class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        else:
            dict = {}
            for i in range (len(s)):
                if s[i] not in dict:
                    dict[s[i]]=1
                else:
                    dict[s[i]]+=1
                    
            for j in range(len(t)):
                if t[j] not in dict or dict[t[j]]==0:
                    return False
                dict[t[j]]-=1

            for value in dict.values():
                if value!=0:
                    return False
                return True
                    
                    
        