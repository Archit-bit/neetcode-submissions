class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for s in strs:
            sorted_s="".join(sorted(s))
            out[sorted_s]=out.get(sorted_s,[])+[s]
        return list(out.values())

        