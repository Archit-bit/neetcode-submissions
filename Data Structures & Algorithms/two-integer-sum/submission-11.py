class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for n in range(len(nums)):
            comp=target-nums[n]
            if comp in seen:
                return [seen[comp],n]
            seen[nums[n]]=n
        