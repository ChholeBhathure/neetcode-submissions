class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for string in strs:
            freq=[0]*26
            for char in string:
                index=ord(char)-ord('a')
                freq[index]+=1
            key=tuple(freq)
            if key not in group:
                group[key]=[]
            group[key].append(string)

        return list(group.values())    
