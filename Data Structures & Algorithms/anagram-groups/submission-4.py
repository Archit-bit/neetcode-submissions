class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sign={}
        for st in strs:
            sign_str="".join(sorted(st))
            if sign_str not in sign:
                sign[sign_str]=[]
            sign[sign_str].append(st)
        return list(sign.values())

        