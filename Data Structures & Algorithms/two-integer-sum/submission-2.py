class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick={}
        for i, n in enumerate(nums):
            num = target-n
            if num in dick:
                return [dick[num],i]
            dick[n]=i
        return []



