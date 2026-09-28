class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for string in strs:
            n=len(string)
            encoded+=str(n)+","+string
        return encoded

    def decode(self, encoded: str) -> List[str]:
        decoded=[]
        i=0
        while i<len(encoded):
            j=i
            while j<len(encoded) and encoded[j]!=',':
                j+=1
            length=int(encoded[i:j])
            i=j+1
            word=encoded[i:length+i]
            decoded.append(word)
            i+=length
        return decoded

