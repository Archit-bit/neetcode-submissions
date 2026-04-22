class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        
        for string in strs:
            sign="".join(sorted(string))
            if sign not in map:
                map[sign]=[]
                
            
            map[sign].append(string)
        return list(map.values())


        