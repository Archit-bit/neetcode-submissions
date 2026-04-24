class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        freq_list=list(freq.items())
        freq_list.sort(key=lambda x:x[1],reverse = True)
        for i in range(k):
            res.append(freq_list[i][0])
        return res
        