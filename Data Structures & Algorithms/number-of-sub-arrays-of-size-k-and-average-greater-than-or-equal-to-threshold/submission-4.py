class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        res=0
        threshold *= k
        if not arr:
            return 0
        cur_sum=0
        for i in range(k):
            cur_sum+=arr[i]
        
        if cur_sum>=threshold:
            res+=1
        for right in range(k,len(arr)):
            cur_sum+=(arr[right]-arr[left])
            if cur_sum>=threshold:
                res+=1
            left+=1
        return res            
                    
            

        