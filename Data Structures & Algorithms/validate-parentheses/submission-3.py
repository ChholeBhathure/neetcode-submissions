class Solution:
    def isValid(self, s: str) -> bool:
        d=[]
        top=0
        for i in s:
            if len(d)!=0:
                top=d[-1]
            if i=="(" or i=="[" or  i=="{":
                d.append(i)
            elif (i==")" or i=="}" or i=="]") and len(d)==0:
                return False
            elif (i==")" and top=="("):
                d.pop()
            elif (i=="}" and top=="{") :
                d.pop()
            elif (i=="]" and top=="["):
                d.pop()
            elif(i==")" and top=="[") or (i==")" and top=="{"):
                return False
            elif(i=="}" and top=="[") or (i=="}" and top=="("):
                return False
            elif(i=="]" and top=="(") or (i=="]" and top=="{"):
                return False
            
        return len(d)==0


        