class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        res=0
        sum=0.0
        if not arr:
            return 0
        for right in range(len(arr)):
            if right<k:
                sum+=arr[right]
                if right==k-1 and sum/k>=threshold: res+=1
                
            else:
                sum+=(arr[right]-arr[left])
                if sum/k>=threshold:
                    res+=1
                left+=1
        return res            
                    
            

        