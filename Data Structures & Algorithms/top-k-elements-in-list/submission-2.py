class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = defaultdict(int)
        res=[]
        n=len(nums)
        nums.sort()
        for x in nums:
            out[x]+=1
        bucket = [[]for _ in range (n+1)]
        for e,v in out.items():
            bucket[v].append(e)
        for i in range(max(out.values()) ,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        


        