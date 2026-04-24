class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        n=len(nums)
        for num in nums:
            freq[num]=freq.get(num,0)+1
        ans=next(k for k,v in freq.items() if v>n/2)
        return ans
        