class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=cursum=0
        prefix={0:1}
        for num in nums:
            cursum+=num
            dif= cursum-k
            res+=prefix.get(dif,0)
            prefix[cursum]=prefix.get(cursum,0)+1
        return res
        