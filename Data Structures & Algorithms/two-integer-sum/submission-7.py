class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=set()
        for i in range(len(nums)):
            num=target-nums[i]
            if num in res:
                return [nums.index(num),i]
            res.add(nums[i])
        return False
        