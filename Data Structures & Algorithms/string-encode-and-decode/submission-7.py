class Solution:
    def encode(self, strs: List[str]) -> str:
        res= ""
        res += "".join(str(len(x)) + "#"+ x for x in strs)
        return res
    def decode(self,strs: list[str]) -> list[str]:
        res=[]
        i = 0
        while i < len(strs):
            j = i
            while strs[j] != "#":
                j+=1
            l= int(strs[i:j])
            i = j+1
            j= i+l
            res.append(strs[i:j])
            i=j
        return res


