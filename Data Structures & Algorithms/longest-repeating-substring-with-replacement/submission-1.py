class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,max_len=0,0
        counts={}
        for r in range(len(s)):
            if s[r] in counts:
                counts[s[r]]+=1
            else:
                counts[s[r]]=1
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]]-=1
                l+=1
            max_len=max(max_len,(r-l+1))

        return max_len
            
                
            


        