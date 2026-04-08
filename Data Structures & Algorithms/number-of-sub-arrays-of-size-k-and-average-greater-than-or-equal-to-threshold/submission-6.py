class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_prod=0
        threshold*=k
        res=0
        if not arr or k>len(arr):
            return 0
        for r in range(k):
            window_prod+=arr[r]
        if window_prod>=threshold:
            res+=1
        for r in range(k,len(arr)):
            window_prod +=(arr[r]-arr[r-k])
            if window_prod>=threshold:
                res+=1
        return res        

                    
            

        