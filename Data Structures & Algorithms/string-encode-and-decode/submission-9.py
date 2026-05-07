class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string="".join(str(len(x))+"#"+x for x in strs)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i <len(s):
            j=i
            while s[j]!="#":
                j+=1
            l=int(s[i:j])
            j+=1
            i=j+l
            res.append(s[j:i])
        return res

