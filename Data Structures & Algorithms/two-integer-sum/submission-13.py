class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in seen:
                return [seen[comp],i]
            if nums[i]not in seen:
                seen[nums[i]]=i
        return []
        