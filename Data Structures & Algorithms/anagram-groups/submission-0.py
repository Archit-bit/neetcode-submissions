class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        out={}

        for s in strs:
            sorteds="".join(sorted(s))
            if sorteds not in out:
                out[sorteds] = []
            out[sorteds].append(s)
        return list(out.values())
        


        