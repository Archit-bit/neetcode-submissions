class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low=0
        high=len(arr)-1
        while low<=high:
            mid= low + (high-low)//2
            if arr[mid]==x:
                low=mid+1
                high=mid-1
                break
            elif arr[mid]>x:
                high=mid-1
            else:
                low=mid+1
        left=high
        right=low

        while (right - left - 1) < k:
            if left<0:
                right+=1
            elif right>=len(arr):
                left-=1
            else:
                if abs(arr[left]-x)<=abs(arr[right]-x):
                    left-=1
                else:
                    right+=1
        return arr[left+1:right]
                
            
                

