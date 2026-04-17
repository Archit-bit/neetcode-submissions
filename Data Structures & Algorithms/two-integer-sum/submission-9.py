class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for i in range(len(nums)):
            num=target-nums[i]
            if num in res:
                return [res[num],i]
            res[nums[i]]=i
        return False
        