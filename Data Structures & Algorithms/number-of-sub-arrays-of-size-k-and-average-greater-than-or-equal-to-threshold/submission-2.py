class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        res=0
        
        if not arr:
            return 0
        cur_sum=sum(arr[:k])
        
        if cur_sum/k>=threshold:
            res+=1
        for right in range(k,len(arr)):
            cur_sum+=(arr[right]-arr[left])
            if cur_sum/k>=threshold:
                res+=1
            left+=1
        return res            
                    
            

        