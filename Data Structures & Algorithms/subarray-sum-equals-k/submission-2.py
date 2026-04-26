class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=cur_sum=0
        prefix={0:1}
        for num in nums:
            cur_sum+=num
            
            dif=cur_sum-k
            res+=prefix.get(dif,0)
            prefix[cur_sum]=prefix.get(cur_sum,0)+1
        return res
