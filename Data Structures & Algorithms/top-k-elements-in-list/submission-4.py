class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        ans=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        pair=list(freq.items())
        pair.sort(key=lambda x:x[1],reverse=True)
        for i in range(k):
            ans.append(pair[i][0])
        return ans

        

        