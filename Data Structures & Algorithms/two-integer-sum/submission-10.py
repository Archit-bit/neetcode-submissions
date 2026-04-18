class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            compt=target-nums[i]
            if compt in seen:
                return[seen[compt],i]
            
            seen[nums[i]]=i
        