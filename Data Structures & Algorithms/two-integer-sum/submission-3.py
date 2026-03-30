class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,n in enumerate(nums):
            needed = target-n
            
            if needed in dic:
                return[dic[needed],i]
            dic[n]=i
        #print(dic)

        # dick={}
        # for i, n in enumerate(nums):
        #     num = target-n
        #     if num in dick:
        #         return [dick[num],i]
        #     dick[n]=i
        # return []


